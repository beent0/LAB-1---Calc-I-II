import interacao
#O import serve para ir buscar código a outro ficheiro/módulo
#Caso não esteja na mesma pasta é necessário definir o diretório completo


def main():
    i = interacao.Interacao()
    i.executar()

if __name__ == '__main__':
    main()