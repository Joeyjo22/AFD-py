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
    afd = {
        "alfabeto": {"a", "b", "c"},
        "inicio": "q0",
        "finales": {"q0", "q2"},
        "delta": {
            # Desde q0 (Par de 'a', listo para recibir cualquier cosa menos 'c' tras 'b')
            ("q0", "a"): "q1",
            ("q0", "b"): "q2",
            ("q0", "c"): "q0",
            
            # Desde q1 (Impar de 'a')
            ("q1", "a"): "q0",
            ("q1", "b"): "q3",
            ("q1", "c"): "q1",
            
            # Desde q2 (Par de 'a', último fue 'b')
            ("q2", "a"): "q1",
            ("q2", "b"): "q2",
            ("q2", "c"): "q4", # ERROR: Subcadena "bc" detectada
            
            # Desde q3 (Impar de 'a', último fue 'b')
            ("q3", "a"): "q0",
            ("q3", "b"): "q3",
            ("q3", "c"): "q4", # ERROR: Subcadena "bc" detectada
            
            # q4 es un estado sumidero (dead state), no tiene salidas exitosas
        }
    }

    w = input("Cadena (a,b,c): ").strip()
    ok, rec = acepta(afd, w)

    print("Recorrido:", " -> ".join(rec))
    print("ACEPTADA" if ok else "RECHAZADA")


if __name__ == "__main__":
    main()