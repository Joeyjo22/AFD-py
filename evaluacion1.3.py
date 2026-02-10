def acepta(afd, w):
    estado = afd["inicio"]
    rec = [estado]

    for s in w:
        if s not in afd["alfabeto"]:
            return False, rec

        if (estado, s) not in afd["delta"]:
            return False, rec

        estado = afd["delta"][(estado, s)]
        rec.append(estado)

    return (estado in afd["finales"]), rec


def main():
    # q0_p0: 0 '1's, par '0's (Aceptación inicial: cadena vacía o 00...)
    # q0_i0: 0 '1's, impar '0's
    # qP_p: Par de '1's (>0), último bloque de '0's es par
    # qP_i: Par de '1's (>0), último bloque de '0's es impar (Aceptación)
    # qI_p: Impar de '1's, último bloque de '0's es par (Aceptación)
    # qI_i: Impar de '1's, último bloque de '0's es impar

    afd = {
        "alfabeto": {"0", "1"},
        "inicio": "q0_p0",
        "finales": {"q0_p0", "qP_i", "qI_p"},
        "delta": {
            # Regla 1: Sin '1's (Estados q0_...)
            ("q0_p0", "0"): "q0_i0",
            ("q0_p0", "1"): "qI_p", # Pasa a regla de impar de '1's
            ("q0_i0", "0"): "q0_p0",
            ("q0_i0", "1"): "qI_p",

            # Regla 2: Par de '1's (>0)
            ("qP_p", "0"): "qP_i", # Un '0' hace que el bloque final sea impar
            ("qP_p", "1"): "qI_p", # Vuelve a impar de '1's
            ("qP_i", "0"): "qP_p", # Otro '0' hace que el bloque final sea par
            ("qP_i", "1"): "qI_p",

            # Regla 3: Impar de '1's
            ("qI_p", "0"): "qI_i",
            ("qI_p", "1"): "qP_p", # Pasa a par de '1's
            ("qI_i", "0"): "qI_p",
            ("qI_i", "1"): "qP_p"
        }
    }

    w = input("Cadena (0,1): ").strip()
    ok, rec = acepta(afd, w)

    print("Recorrido:", " -> ".join(rec))
    print("ACEPTADA" if ok else "RECHAZADA")


if __name__ == "__main__":
    main()