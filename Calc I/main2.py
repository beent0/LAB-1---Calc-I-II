import diferenca
import soma
import divisao
import multiplicacao
import raizquadrada

def main():
    print("Introduza dois números: ")
    x: float = float(input("x= "))
    y: float = float(input("y= "))

    subtrair = diferenca.subtrair(x, y)
    somar = soma.somar(x, y)
    dividir = divisao.dividir(x, y)
    raiz_quadrada = raizquadrada.raizquadrada(x)
    multiplicar = multiplicacao.multiplicar(x, y)

    print("O resultado da subtração é: ", subtrair)
    print("O resultado da soma é: ", somar)
    print("O resultado da divisão é: ", dividir)
    print("O resultado da multiplicação é: ", multiplicar)
    print("O resultado da raíz quadrada do primeiro número é: ", raiz_quadrada)



if __name__ == '__main__':
    main()
