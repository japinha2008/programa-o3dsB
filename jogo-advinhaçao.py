import random

# Número secreto entre 1 e 10
numero_secreto = random.randint(1, 10)

tentativas = 5
contador = 0

print("🎯 Bem-vindo ao jogo de adivinhação!")
print("Você tem 5 tentativas para descobrir o número secreto entre 1 e 10.")

while contador < tentativas:
    palpite = int(input("Digite seu palpite: "))
    contador += 1

    if palpite == numero_secreto:
        print("✅ Parabéns! Você acertou o número secreto!")
        break
    else:
        print("❌ Errou!")

        # Regra do bônus: se a diferença for apenas 1, ganha +1 tentativa
        if abs(palpite - numero_secreto) == 1:
            tentativas += 1
            print("🎁 Você chegou muito perto! Ganhou uma tentativa extra.")

        # Mostrar quantas tentativas restam
        print(f"Tentativas restantes: {tentativas - contador}")

if palpite != numero_secreto:
    print(f"🔒 Fim de jogo! O número secreto era {numero_secreto}.")
