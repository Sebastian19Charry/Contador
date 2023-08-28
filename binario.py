from contador import Contador

class Binario(Contador):
    def obtener_valor(self):
        return bin(self.valor)[2:]