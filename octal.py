from contador import Contador

class Octal(Contador):
    def obtener_valor(self):
        return oct(self.valor)[2:]