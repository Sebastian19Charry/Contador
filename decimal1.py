from contador import Contador

class Decimal(Contador):
    def obtener_valor(self):
        return str(self.valor)