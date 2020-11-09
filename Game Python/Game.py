from models.calcular import Calcular


def main() -> None:
    pontos: int = 0
    jogar(pontos)


def jogar(pontos: int) -> None:
    dificuldade: int = int(input('Informe o nível de dificuldade desejado [ 1 - ENEM, 2 - UFPR, 3 - USP, 4 - ITA]: '))

    calc: Calcular = Calcular(dificuldade)

    print(f'{dificuldade}:Informe o resultado para a seguinte operação: ')
    calc.mostrar_operacao()

    resultado: int = int(input())

    if calc.checar_resultados(resultado):
        pontos += 1
        print(f'Você tem {pontos} ponto(s)')

    continuar: int = int(input('Deseja continuar no jogo ? [1 - SIM ou 0 - NÃO]'))

    if continuar:
        jogar(pontos)
    else:
        print(f'Você finalizou com {pontos} ponto(s).')
        print('Até a próxima!')


if __name__ == '__main__':
    main()
