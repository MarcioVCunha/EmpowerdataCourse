# jogo da adivinhação
from random import randint

numero_secreto = randint(1, 5)
numero_escolhido = 0

while numero_secreto != numero_escolhido:
    numero_escolhido = int(input("Escolha um numero de 1 a 5:"))

print(f"Parabéns! Você descobriu que o numero secreto era o {numero_secreto}")
