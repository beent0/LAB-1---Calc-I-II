from Operacoes import dividir, subtrair, multiplicar, somar, sqrt



def main():
    print("Qual é o cálculo que quer efetuar? * + - / sqrt")
    res:str = input()
    print("Preciso que introduza dois valores:")
    x:float = float(input("x="))
    y:float = float(input("y="))
    if res =="+":
        s:object = somar.Somar(x, y)
        res = s.executar()
        print("O valor da operação somar é: ", res)
    elif res =="/":
        s:object = dividir.Dividir(x, y)
        res = s.executar()
        if type(res)==str:
            print (res)
        else:
            print("O valor da operação divisão é: ", res)
    elif res == "-":
        s:object = subtrair.Subtrair(x, y)
        res = s.executar()
        print("O valor da subtração é: ", res)
    elif res == "*":
        s:object = multiplicar.Multiplicar(x, y)
        res = s.executar()
        print("O valor da Multiplicação é: ", res)
    elif res == "sqrt":
        s:object = sqrt.Sqrt(x, y)
        resx = s.executarx()
        resy = s.executary()
        print("O resultado da raiz de x é: ", resx, " e de y: ", resy)

if __name__ == '__main__':
    main()
