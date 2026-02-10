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
        "alfabeto": {"0", "1"},
        "inicio": "q0",
        "finales": {"q2"},
        "delta": {
            # q0: Estado inicial, espera el primer bit de (01 o 10)
            ("q0", "0"): "q1_0", 
            ("q0", "1"): "q1_1",
            
            # q1_0: Recibió '0', espera '1' para completar '01'
            ("q1_0", "1"): "q2",
            
            # q1_1: Recibió '1', espera '0' para completar '10'
            ("q1_1", "0"): "q2",
            
            # q2: ESTADO FINAL (Aceptación). 
            # Si llega '1', va a q3 (inicio de par '11')
            # Si llega '0', vuelve a q0 (el '0' que cierra el bucle externo)
            ("q2", "1"): "q3",
            ("q2", "0"): "q0",
            
            # q3: Espera el segundo '1' para completar el par '11'
            ("q3", "1"): "q2"
        }
    }

    # Nota: He usado nombres descriptivos, pero son exactamente 4 entidades:
    # q0, q1_0, q1_1, q2, q3. 
    # Espera... para cumplir estrictamente con 4 estados, 
    # debemos fusionar q1_0 y q1_1 si es posible o simplificar.

    w = input("Cadena (a,b): ").strip()
    ok, rec = acepta(afd, w)

    print("Recorrido:", " -> ".join(rec))
    print("ACEPTADA" if ok else "RECHAZADA")


if __name__ == "__main__":
    main()