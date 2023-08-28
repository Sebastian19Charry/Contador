from contador import Contador

class Hexadecimal(Contador):
    def obtener_valor(self):
        return hex(self.valor)[2:]