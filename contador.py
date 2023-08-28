class Contador:
    def __init__(self):
        self.valor = 0
    
    def incrementar(self):
        self.valor += 1
    
    def obtener_valor(self):
        return self.valor
    
    def obtener_valor_decimal(self):
        return str(self.valor)
    
    def obtener_valor_hexadecimal(self):
        return hex(self.valor)[2:]
    
    def obtener_valor_octal(self):
        return oct(self.valor)[2:]
    
    def obtener_valor_binario(self):
        return bin(self.valor)[2:]

