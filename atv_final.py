import random
import os

list = [i for i in range(1,10)]
board = [[i+1 for i in range(3)] for j in range(3)]

cont=0
for l in range(3):
    for c in range(3):
        board[l][c] = list[cont]
        cont+=1

list.remove(5)
list_movic = [5]
list_movip = []
board[1][1] = "X"

def imagem():
    imagem = f"""
    +-------+-------+-------+
    |       |       |       |
    |   {board[0][0]}   |   {board[0][1]}   |   {board[0][2]}   |
    |       |       |       |
    +-------+-------+-------+
    |       |       |       |
    |   {board[1][0]}   |   {board[1][1]}   |   {board[1][2]}   |
    |       |       |       |
    +-------+-------+-------+
    |       |       |       |
    |   {board[2][0]}   |   {board[2][1]}   |   {board[2][2]}   |
    |       |       |       |
    +-------+-------+-------+
    """
    print(imagem)

def venceu():
    #Checar se Jogador venceu

    if len(list_movic) >=3 or len(list_movip) >=3:
        #Linha horizontal
        if 1 in list_movic and 2 in list_movic and 3 in list_movic or 4 in list_movic and 5 in list_movic and 6 in list_movic or 7 in list_movic and 8 in list_movic and 9 in list_movic:
            print("O computador venceu!")
            return True
        
        #Linha vertical
        if 1 in list_movic and 4 in list_movic and 7 in list_movic or 2 in list_movic and 5 in list_movic and 8 in list_movic or 3 in list_movic and 6 in list_movic and 9 in list_movic:
            print("O computador venceu!")
            return True
        
        #linha diagonal
        if 1 in list_movic and 5 in list_movic and 9 in list_movic or 7 in list_movic and 5 in list_movic and 3 in list_movic:
            print("O computador venceu!")
            return True
        
        #Checar se Jogador venceu

        #Linha horizontal
        if 1 in list_movip and 2 in list_movip and 3 in list_movip or 4 in list_movip and 5 in list_movip and 6 in list_movip or 7 in list_movip and 8 in list_movip and 9 in list_movip:
            print("O jogador venceu!")
            return True
        
        #Linha vertical
        if 1 in list_movip and 4 in list_movip and 7 in list_movip or 2 in list_movip and 5 in list_movip and 8 in list_movip or 3 in list_movip and 6 in list_movip and 9 in list_movip:
            print("O jogador venceu!")
            return True
        
        #linha diagonal
        if 1 in list_movip and 5 in list_movip and 9 in list_movip or 7 in list_movip and 5 in list_movip and 3 in list_movip:
            print("O jogador venceu!")
            return True


    return False
imagem()

def atualizar_movimentos():

    if num_movimento%3 == 0:
        board[(num_movimento//3)-1][(num_movimento%3)-1] = "O"
    else:
        board[num_movimento//3][(num_movimento%3)-1] = "O"
    list.remove(num_movimento)
    list_movip.append(num_movimento)

    if venceu() == False:    
        computador_movimento = random.choice(list)
        print(computador_movimento)
        if computador_movimento%3 == 0:
            board[(computador_movimento//3)-1][(computador_movimento%3)-1] = "X"
        else:
            board[computador_movimento//3][(computador_movimento%3)-1] = "X"
        list.remove(computador_movimento)
        list_movic.append(computador_movimento)
    
def reiniciar():
    list = [1,2,3,4,5,6,7,8,9]
    board = [[i+1 for i in range(3)] for j in range(3)]
    cont=0

    for l in range(3):
        for c in range(3):
            board[l][c] = list[cont]
            cont+=1

    list.remove(5)
    list_movic = [5]
    list_movip = []
    board[1][1] = "X"
    return list, list_movic, list_movip, board
    
jogo = True

while jogo:
    
    num_movimento = input("Digite seu movimento: ")
    

    if num_movimento == "":
        print("Ops você não digitou nada!")
        input()
    
    elif "r" in num_movimento.lower():
        print("Reiniciou")
        input()
        list, list_movic, list_movip, board = reiniciar()
    else:
        
        num_movimento = int(num_movimento)
        if num_movimento == 10:
            break
        if num_movimento not in list or "":
            print("Ops esse movimento não é possível")
            input()
        else:
            atualizar_movimentos()
    os.system("cls")
    print("\n")

    print("Jogadas PC: ", list_movic)
    print("Jogadas Player: ", list_movip)
    print("Jogadas Possíveis: ", list, "\n", len(list))

    imagem()

    #empate
    if len(list) == 0:
        while True:
            resp = input("EMPATE \n Deseja continuar? SIM ou NÃO?").lower()
            print(resp)
            if resp == "sim":
                list, list_movic, list_movip, board = reiniciar()
                os.system("cls")
                imagem()
                break
            elif resp == "não" or resp == "nao":
                jogo = False
                break
            else:
                input("Ops o comando digitado não é válido tente novamente!")
                
    #venceu
    if venceu() == True:
        while True:
            resp = input("O jogo terminou! \n Deseja continuar? SIM ou NÃO? ")
            
            if resp == "sim":
                list, list_movic, list_movip, board = reiniciar()
                os.system("cls")
                imagem()
                break
            elif resp == "não" or resp == "nao":
                jogo = False
                os.system("cls")
                break
            else:
                input("Ops o comando digitado não é válido tente novamente!")