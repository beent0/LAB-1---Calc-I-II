class Subtrair:
    def __init__(self, x:float, y:float):
        self.x = x
        self.y = y
        self.res = 0


    def executar(self)->float:
        """
        Subtrai dois números
        :param x: valor subtraido
        :param y: valor a subtrair
        :return: retorna o resultado da subtraçao
        """
        self.res = self.x - self.y
        return self.res