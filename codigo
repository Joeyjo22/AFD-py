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
        "alfabeto": {"a", "b"},
        "inicio": "q0",
        "finales": {"q2"},
        "delta": {
            ("q0", "a"): "q1",
            ("q1", "a"): "q1",
            ("q1", "b"): "q2"
        }
    }

    w = input("Cadena (a,b): ").strip()
    ok, rec = acepta(afd, w)

    print("Recorrido:", " -> ".join(rec))
    print("ACEPTADA" if ok else "RECHAZADA")


if __name__ == "__main__":
    main()
 
