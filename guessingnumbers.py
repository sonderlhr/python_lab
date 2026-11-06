import random

numero_secreto = random.randint(1, 100)

print("=== Jogo de Adivinhação ===")
print("Tente adivinhar o número entre 1 e 100!")

tentativas = 0

while True:
    palpite = int(input("Digite seu palpite: "))
    tentativas += 1

    if palpite < numero_secreto:
        print("O número secreto é maior!")

    elif palpite > numero_secreto:
        print("O número secreto é menor!")

    else:
        print(f"Parabéns! Você acertou em {tentativas} tentativas!")
        break