class Multiplicar:
    def __init__(self, x:float, y:float):
        self.x = x
        self.y = y
        self.res = 0


    def executar(self)->float:
        """
        Multiplica dois números
        :param x: valor 1
        :param y: valor 2
        :return: retorna o resultado da multiplicação
        """
        self.res = self.x * self.y
        return self.res