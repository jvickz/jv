import random


def pedra_papel_tesoura():
    opcoes = ["Pedra", "Papel", "Tesoura"]
    print("Bem-vindo ao jogo de Pedra, Papel e Tesoura!")

    while True:
        computador = random.choice(opcoes)
        jogador = input(
            "Escolha Pedra, Papel ou Tesoura (ou 'sair' para terminar): ").capitalize()

        if jogador == 'Sair':
            print("Obrigado por jogar! Até a próxima.")
            break
        elif jogador not in opcoes:
            print("Escolha inválida. Tente novamente.")
            continue

        print(f"\nVocê escolheu: {jogador}")
        print(f"O computador escolheu: {computador}\n")

        if jogador == computador:
            print("Empate!")
        elif (jogador == "Pedra" and computador == "Tesoura") or \
             (jogador == "Papel" and computador == "Pedra") or \
             (jogador == "Tesoura" and computador == "Papel"):
            print("Você venceu!")
        else:
            print("O computador venceu!")

        print("\nVamos jogar novamente!")


pedra_papel_tesoura()
