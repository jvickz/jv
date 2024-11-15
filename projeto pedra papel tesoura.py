import random


def pedra_papel_tesoura():
    opcoes = ["Pedra", "Papel", "Tesoura"]
    print("Bem vindo ao jogo de Pedra, Papel e Tesoura!")

    while True:
        computador = random.choice(opcoes)
        jogador = input(
            "Escolha Pedra, Papel ou tesoura (ou 'sair' para terminar): ").capitalize()

        if jogador == 'sair':
            print("Obrigado por jogar Até a próxima.")
            break
        elif jogador not in opcoes:
            print("Escolha inválida. Tente novamente.")
            continue
        print(f"\nVocê escolheu: {jogador}")
        print(f"O computador escolheu: {computador}\n")

        if jogador == computador:
            print("Empate!")
        elif (jogador == "pedra" and computador == "tesoura") or \
            (jogador == "Papel" and computador == "Pedra") or\
                (jogador == "Tesoura" and computador == "Papel"):
            print("Você venceu!")
        else:
            print("O computador venceu!")

        print("\nVAmos jogar Novamente!")

        pedra_papel_tesoura
