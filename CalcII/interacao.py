from Operacoes import dividir, subtrair, multiplicar, somar, sqrt



class Interacao:
    def __init__(self):
        pass

    def executar(self):
        print("Preciso que introduza dois valores:")
        x: float = float(input("x="))
        y: float = float(input("y="))

        # Soma
        somar_somar = somar.Somar(x, y)
        s: object = somar_somar
        resSoma = s.executar()
        print("O valor da operação somar é: ", resSoma)

        # Subtração
        s: object = subtrair.Subtrair(x, y)
        resSubtracao = s.executar()
        print("O valor da subtração é: ", resSubtracao)

        # Multiplicação
        s: object = multiplicar.Multiplicar(x, y)
        resMulti = s.executar()
        print("O valor da Multiplicação é: ", resMulti)

        # Divisão
        s: object = dividir.Dividir(x, y)
        resDiv = s.executar()
        if type(resDiv) == str:
            print(resDiv)
        else:
            print("O valor da operação divisão é: ", resDiv)

        # Sqrt
        s: object = sqrt.Sqrt(x, y)
        resx = s.executarx()
        resy = s.executary()
        print("O resultado da raiz de x é: ", resx, " e de y: ", resy)