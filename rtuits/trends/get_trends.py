from models import Trend	
class Modelo:

    def __init__(self):
        self.divisor = 23
        valor = 4
        resultado = self.devolver_resultado(valor)
        print "%d/%d es %d" % (valor, self.divisor, resulatdo)

    def devolver_resultado(self, numero):
        resultado = numero//self.divisor
        return resultado

