class SolitaireCipher:
    def __init__(self):
        self.baraja = list(range(1, 55))

    def mover_comodines(self):
        idx_a = self.baraja.index(53)
        nueva_pos_a = (idx_a + 1) % len(self.baraja)
        self.baraja.pop(idx_a)
        self.baraja.insert(nueva_pos_a, 53)
        idx_b = self.baraja.index(54)
        nueva_pos_b = (idx_b + 2) % len(self.baraja)
        self.baraja.pop(idx_b)
        self.baraja.insert(nueva_pos_b, 54)

    def mostrar_estado(self, mensaje):
        print(f"[*] {mensaje}:")
        print(self.baraja[:10], "... [cartas intermedias] ...", self.baraja[-5:])
        print("-" * 50)

if __name__ == "__main__":
    print("🃏 Inicializando Cifrado Solitario por Cartomagia...\n")
    
    cifrador = SolitaireCipher()
    cifrador.mostrar_estado("Baraja recién ordenada")
    cifrador.mover_comodines()
    cifrador.mostrar_estado("Baraja tras mover comodines (A y B)")