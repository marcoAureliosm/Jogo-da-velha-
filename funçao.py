def tabuleiro ():
    velha = """               Posições
       |   |      0 | 1 | 2
    ---+---+---  ---+---+---
       |   |      3 | 4 | 5
    ---+---+---  ---+---+---
       |   |      6 | 7 | 8
    """
    print('============JOGO DA VELHA===============')
    print(velha)
def jogo():
    matriz = ['', '', '',
              '', '', '',
              '', '', '']

    print("Jogador 1 = X e Jogador 2 = O")

    sair = "S"
    repetir = 2
    velha = 0
    jogadas = 1

    nomeUm = str(input("Digite o nome do primeiro jogador: "))
    nomeDois = str(input("Digite o nome do segundo jogador: "))

    while sair == "S":
        for i in range(1,9):
            if repetir % 2 == 0:

                linha = int(input(nomeUm + ", faça sua jogada = X : "))
                if matriz[linha] == '':
                    matriz[linha] = 'X'
                else:
                    print("Jogada inválida, tente novamente !")
                    linha = int(input(nomeUm + ", faça sua jogada: "))
                    matriz[linha] = 'X'

                print('\t %s | %s | %s ' % (matriz[0], matriz[1], matriz[2]))
                print('\t---------')
                print('\t %s | %s | %s ' % (matriz[3], matriz[4], matriz[5]))
                print('\t----------')
                print('\t %s | %s | %s ' % (matriz[6], matriz[7], matriz[8]))

            else:
                linha = int(input(nomeDois + ", faça sua jogada = O : "))
                if matriz[linha] == '':
                    matriz[linha] = 'O'
                else:
                    print("Jogada inválida, tente novamente !")
                    linha = int(input(nomeDois + ", faça sua jogada: "))
                    matriz[linha] = 'O'

                print('\t %s | %s | %s ' % (matriz[0], matriz[1], matriz[2]))
                print('\t---------')
                print('\t %s | %s | %s ' % (matriz[3], matriz[4], matriz[5]))
                print('\t----------')
                print('\t %s | %s | %s ' % (matriz[6], matriz[7], matriz[8]))

            repetir += 1
                #HORIZONTAL
                #LISTA VENCEDOR X

            if ((matriz[0] =='X'))and((matriz[1] =='X')) and ((matriz[2] =='X')):
                print(nomeUm + " foi o ganhador !!")
                print('============FIM DE JOGO===============')
                break
            elif((matriz[3] =='X'))and((matriz[4] =='X')) and ((matriz[5] =='X')):
                print(nomeUm + " foi o ganhador !!")
                print('============FIM DE JOGO===============')
                break
            elif ((matriz[6] == 'X')) and ((matriz[7] == 'X')) and ((matriz[8] == 'X')):
                print(nomeUm + " foi o ganhador !!")
                print('============FIM DE JOGO===============')
                break
                #COLUNAS
            elif ((matriz[0] == 'X')) and ((matriz[3] == 'X')) and ((matriz[6] == 'X')):
                print(nomeUm + " foi o ganhador !!")
                print('============FIM DE JOGO===============')
                break
            elif ((matriz[1] == 'X')) and ((matriz[4] == 'X')) and ((matriz[7] == 'X')):
                print(nomeUm + " foi o ganhador !!")
                print('============FIM DE JOGO===============')
                break
            elif ((matriz[2] == 'X')) and ((matriz[5] == 'X')) and ((matriz[8] == 'X')):
                print(nomeUm + " foi o ganhador !!")
                print('============FIM DE JOGO===============')
                break
                #ATRAVESSADO
            elif ((matriz[2] == 'X')) and ((matriz[4] == 'X')) and ((matriz[6] == 'X')):
                print(nomeUm + " foi o ganhador !!")
                print('============FIM DE JOGO===============')
                break
            elif ((matriz[0] == 'X')) and ((matriz[4] == 'X')) and ((matriz[8] == 'X')):
                print(nomeUm + " foi o ganhador !!")
                print('============FIM DE JOGO===============')
                break
              #LISTA VENCEDOR O
                #COLUNAS
            if ((matriz[0] =='O'))and((matriz[1] =='O')) and ((matriz[2] =='O')):
                print(nomeDois + " foi o ganhador !!")
                print('============FIM DE JOGO===============')
                break
            elif((matriz[3] =='O'))and((matriz[4] =='O')) and ((matriz[5] =='O')):
                print(nomeDois + " foi o ganhador !!")
                print('============FIM DE JOGO===============')
                break
            elif ((matriz[6] == 'O')) and ((matriz[7] == 'O')) and ((matriz[8] == 'O')):
                print(nomeDois + " foi o ganhador !!")
                print('============FIM DE JOGO===============')
                break
                #COLUNAS
            elif ((matriz[0] == 'O')) and ((matriz[3] == 'O')) and ((matriz[6] == 'O')):
                print(nomeDois + " foi o ganhador !!")
                print('============FIM DE JOGO===============')
                break
            elif ((matriz[1] == 'O')) and ((matriz[4] == 'O')) and ((matriz[7] == 'O')):
                print(nomeDois + " foi o ganhador !!")
                print('============FIM DE JOGO===============')
                break
            elif ((matriz[2] == 'O')) and ((matriz[5] == 'O')) and ((matriz[8] == 'O')):
                print(nomeDois + " foi o ganhador !!")
                print('============FIM DE JOGO===============')
                break
                #ATRAVESSADO
            elif ((matriz[2] == 'O')) and ((matriz[4] == 'O')) and ((matriz[6] == 'O')):
                print(nomeDois + " foi o ganhador !!")
                print('============FIM DE JOGO===============')
                break
            elif ((matriz[0] == 'O')) and ((matriz[4] == 'O')) and ((matriz[8] == 'O')):
                print(nomeDois + " foi o ganhador !!")
                print('============FIM DE JOGO===============')
                break
        else:
            print('JOGO EMPATADO')
            print('============FIM DE JOGO===============')
            break

        sair = str(input('DESEJA JOGAR NOVAMENTE?[S]sim ou [N]não'))
        
        if sair == 'S':
            matriz = ['', '', '',
                      '', '', '',
                      '', '', '']
            print (matriz)
     

tabuleiro()
jogo()
