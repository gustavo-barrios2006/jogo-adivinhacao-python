print("* Bem vindo ao jogo de adivinhação *")
numero_secreto=42
total_de_tentativas=3
for rodada in range(1, total_de_tentativas+1):
    print("Rodada {} de {}".format(rodada, total_de_tentativas))
    chute=int(input("Digite seu chute"))
    if(chute==numero_secreto):
        print("Você acertou!")
        break
    elif chute<numero_secreto:
        print("Você errou! O seu chute foi menor que o número secreto.")
    else:
        print("Você errou! O seu chute foi maior que o número secreto.")
print("Fim do jogo")