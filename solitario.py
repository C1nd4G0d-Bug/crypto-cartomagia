def crear_baraja():
    return list(range(1, 55))

def mostrar_baraja(baraja, etapa):
    print(f"[*] {etapa}:")
    print(baraja)
    print("-" * 50)

if __name__ == "__main__":
    print("🃏 Iniciando el entorno criptográfico Solitario...\n")
    baraja_actual = crear_baraja()
    mostrar_baraja(baraja_actual, "Baraja inicial en orden de fábrica")