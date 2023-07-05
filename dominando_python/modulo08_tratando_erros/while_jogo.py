# jogo da adivinhação
from random import randint

def login():
    print("**************************************")
    print("Seja bem vindo ao jogo de adivinhação!")
    print("**************************************")

def game_loop(numero_secreto, numero_escolhido):
    while True:
        try:
            numero_escolhido = int(input("Escolha um numero de 1 a 5:"))
        except:
            print("Você escolheu um número inválido")
        else:
            if(numero_escolhido not in (1, 2, 3, 4, 5)):
                print("Número precisa estar entre 1 e 5!")
                continue
            elif numero_escolhido == numero_secreto:
                print(f"Parabens, você acertou o numero secreto: {numero_secreto}")
                break
            else:
                print("Número incorreto :(")


def start_game():
    
    login()

    numero_secreto = randint(1, 5)
    numero_escolhido = 0

    game_loop(numero_secreto, numero_escolhido)
    
start_game()