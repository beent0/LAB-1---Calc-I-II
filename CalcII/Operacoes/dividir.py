from typing import Union

class Dividir:
    def __init__(self, x:float, y:float):
        self.x = x
        self.y = y
        self.res = 0


    def executar(self)->Union[float,str]:
        """
        Divide dois números
        :param x: valor numerador
        :param y: valor denominador
        :return: retorna o resultado da divisão
        """
        try:
            self.res = self.x / self.y
        except ZeroDivisionError:
            return "error:dividing by zero"
        return self.res
