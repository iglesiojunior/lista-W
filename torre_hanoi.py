import random
import os
import time

def contador_proximo_jogo():
    for i in range(6):
        print(f"Começando o próximo jogo em: {i}...")
        time.sleep(1)
        limpar_console()

def mostrar_menu():
    menu = """
    \t===========Torre de Hanói===========
    \t1 - Nível Básico
    \t2 - Nível Intermediário
    \t3 - Nível Avançado 
    \t0 - Encerrar programa
    \t====================================
    """
    print(menu)
def vencedor_jogo(contador_jogador_one, contador_jogador_two):
    if contador_jogador_two > contador_jogador_one:
        print("\tO resultado da partida foi: O Jogador 1 foi o vencedor")
    elif contador_jogador_two < contador_jogador_one:
        print("\tO resultado da partida foi: O Jogador 2 foi o vencedor")
    else:
        print("\tO resultado da partida foi: Empate!")

def rodada(estado_torres, torre_R, torre_G, torre_B, nome_jogador):
    contador_rodada = 0
    while(estado_torres == False):
        print(f"Jogador: {nome_jogador}")
        print(f"Movimentos: {contador_rodada}")
        mostrar_torres_vericalmente(torre_R, torre_G, torre_B)
        movimento_rodada = receber_movimento("Insira um novo movimento: ")
        realizar_movimento(movimento_rodada, torre_R, torre_G, torre_B)
        contador_rodada +=1
        estado_torres = verificar_estado_torres(torre_R, torre_G, torre_B)
        limpar_console()
    print("Parabéns, você completou o desafio!!")
    print(f"Você fez {contador_rodada} movimentos!!")
    return contador_rodada

def limpar_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def realizar_movimento(entrada, torre_R: list, torre_G: list, torre_B: list):
    origem = entrada[0]#string responsável por armazenar a torre de origem
    destino = entrada[1]#string responsável por armazenar a torre de destino
    indice = {"r": torre_R, "g": torre_G, "b": torre_B, "R": torre_R, "G": torre_G, "B": torre_B}
    torre_origem = indice[origem]
    torre_destino = indice[destino]
    if not torre_origem:
        print("Torre de origem vazia!")
        return
    torre_destino.append(torre_origem.pop())
    
def receber_movimento(mensagem):
    entrada = input(mensagem)
    
    if entrada not in ["r", "g", "b", "R", "G", "B"] and len(entrada) > 2 or entrada[0] == entrada[1]:
        return receber_movimento(mensagem)
    else:
        return entrada

def mostrar_torres_vericalmente(torre_R, torre_G, torre_B):
    print("""--------------------------------------
    Torre R     Torre G     Torre B""")
    for i in range(9 , 0, -1):
        elemento_R = torre_R[i-1] if i <= len(torre_R) else " "
        elemento_G = torre_G[i-1] if i <= len(torre_G) else " "
        elemento_B = torre_B[i-1] if i <= len(torre_B) else " "
        print(f"{i}     {elemento_R:^6} {elemento_G:^12} {elemento_B:^14}")

def verificar_estado_torres(torre_R, torre_G, torre_B):
    torres = [torre_R, torre_G, torre_B]
    elementos = ["R", "G", "B"]
    for i in range(len(torres)):
        for j in range(len(torres[i])):
            if torres[i][j] != elementos[i] and torres[i][j] != " ":
                return False
    return True

def gerar_elemento_aleatorio():
    elemntos = ["R", "G", "B"]
    return random.choice(elemntos)

def preencher_elementos_torre_aleatorio(torre: list, tamanho_lista):
    for i in range(tamanho_lista):
        torre.append(gerar_elemento_aleatorio())

def main():
    torre_R = []
    torre_G = []
    torre_B = []
    
    mostrar_menu()
    entrada = int(input("\t>>>"))
    limpar_console()
    while(entrada != 0):
        if entrada == 1:
            
            nome_jogador_one = input("Insira o nome do jogador 1: ")
            nome_jogador_two = input("Insira o nome do jogador 2: ")
            
            preencher_elementos_torre_aleatorio(torre_R, 9)
            copia_torre_R_original = torre_R[:]
            copia_torre_G_original = torre_G[:]
            copia_torre_B_original = torre_B[:]
            estado_torres = verificar_estado_torres(torre_R, torre_G, torre_B)
            
            contador_movimentos_player_one = 0
            contador_movimentos_player_two = 0
            #primeiro jogador
            contador_movimentos_player_one = rodada(estado_torres, torre_R, torre_G, torre_B, nome_jogador_one)
            
            contador_proximo_jogo()
            #segundo jogador
            contador_movimentos_player_two = rodada(estado_torres, copia_torre_R_original, copia_torre_G_original, copia_torre_B_original, nome_jogador_two)
            
            vencedor_jogo(contador_movimentos_player_one, contador_movimentos_player_two)
            
        elif entrada == 2:
            
            nome_jogador_one = input("Insira o nome do jogador 1: ")
            nome_jogador_two = input("Insira o nome do jogador 2: ")
            
            preencher_elementos_torre_aleatorio(torre_R, random.randint(3, 6))
            preencher_elementos_torre_aleatorio(torre_G, random.randint(3, 6))
            preencher_elementos_torre_aleatorio(torre_B, random.randint(3, 6))
            
            copia_torre_R_original = torre_R[:]
            copia_torre_G_original = torre_G[:]
            copia_torre_B_original = torre_B[:]
            estado_torres = verificar_estado_torres(torre_R, torre_G, torre_B)
            
            contador_movimentos_player_one = 0
            contador_movimentos_player_two = 0
            
            #primeiro jogador
            contador_movimentos_player_one = rodada(estado_torres, torre_R, torre_G, torre_B, nome_jogador_one)
            
            contador_proximo_jogo()
            
            #segundo jogador
            contador_movimentos_player_two = rodada(estado_torres, copia_torre_R_original, copia_torre_G_original, copia_torre_B_original, nome_jogador_two)
            print("\tParabéns, você completou o desafio!!")
            print(f"\tVocê fez {contador_movimentos_player_one} movimentos!!")
            vencedor_jogo(contador_movimentos_player_one, contador_movimentos_player_two)
        
        elif entrada == 3:
            nome_jogador_one = input("Insira o nome do jogador 1: ")
            nome_jogador_two = input("Insira o nome do jogador 2: ")
            
            preencher_elementos_torre_aleatorio(torre_R, 8)
            preencher_elementos_torre_aleatorio(torre_G, 8)
            preencher_elementos_torre_aleatorio(torre_B, 8)
            
            copia_torre_R_original = torre_R[:]
            copia_torre_G_original = torre_G[:]
            copia_torre_B_original = torre_B[:]
            estado_torres = verificar_estado_torres(torre_R, torre_G, torre_B)
            
            contador_movimentos_player_one = 0
            contador_movimentos_player_two = 0
            
            #primeiro jogador
            contador_movimentos_player_one = rodada(estado_torres, torre_R, torre_G, torre_B, nome_jogador_one)
            
            contador_proximo_jogo()
            #segundo jogador
            contador_movimentos_player_two = rodada(estado_torres, copia_torre_R_original, copia_torre_G_original, copia_torre_B_original, nome_jogador_two)
            print("\tParabéns, você completou o desafio!!")
            print(f"\tVocê fez {contador_movimentos_player_one} movimentos!!")
            vencedor_jogo(contador_movimentos_player_one, contador_movimentos_player_two)
main()