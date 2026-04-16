
palavra_secreta = "girafa".lower()
letras_acertadas = ["_"] * len(palavra_secreta)
tentativas = 6

# Desenhos da forca (6 partes: cabeça, tronco, braço esquerdo, braço direito, perna esquerda, perna direita)
forca = [
    """
     ------
     |    |
          |
          |
          |
          |
    =========
    """,
    """
     ------
     |    |
     O    |
          |
          |
          |
    =========
    """,
    """
     ------
     |    |
     O    |
     |    |
          |
          |
    =========
    """,
    """
     ------
     |    |
     O    |
    /|    |
          |
          |
    =========
    """,
    """
     ------
     |    |
     O    |
    /|\\   |
          |
          |
    =========
    """,
    """
     ------
     |    |
     O    |
    /|\\   |
    /     |
          |
    =========
    """,
    """
     ------
     |    |
     O    |
    /|\\   |
    / \\   |
          |
    =========
    """
]

print("Bem-vindo ao jogo da Forca!")
print(" ".join(letras_acertadas))

while tentativas > 0 and "_" in letras_acertadas:
    palpite = input("Digite uma letra: ").lower().strip()

    # Usando count() para verificar se a letra aparece na palavra
    if palavra_secreta.count(palpite) > 0:
        # Usando enumerate() e replace() para atualizar as letras acertadas
        for index, letra in enumerate(palavra_secreta):
            if letra == palpite:
                letras_acertadas[index] = letra
        print("Boa! Você acertou uma letra.")
    else:
        tentativas -= 1
        print("Letra incorreta.")
        print(forca[6 - tentativas])  # Mostra o desenho da forca correspondente
        print(f"Você tem {tentativas} tentativas restantes.")

    print(" ".join(letras_acertadas).upper())  # Mostra as letras em maiúsculo

if "_" not in letras_acertadas:
    print("Parabéns, você ganhou!")
else:
    print("Que pena, você perdeu. A palavra era:", palavra_secreta.upper())
