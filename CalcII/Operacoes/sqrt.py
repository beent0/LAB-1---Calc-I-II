class Sqrt:
    def __init__(self, x:float, y:float):
        self.x = x
        self.y = y
        self.resx = 0
        self.resy = 0


    def executarx(self)->float:
        """
        Faz a Raiz Quadrada do número
        :param x: valor
        :return: retorna o resultado da raiz
        """
        self.resx = self.x ** 0.5
        return self.resx

    def executary(self)->float:
        """
        Faz a Raiz Quadrada do número
        :param y: valor
        :return: retorna o resultado da raiz
        """
        self.resy = self.y ** 0.5
        return self.resy