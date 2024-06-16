print("* Bem vindo ao jogo de adivinhação *")
numero_secreto=42
chute=int(input("Digite seu chute"))
if(chute==numero_secreto):
    print("Você acertou!")
elif chute<numero_secreto:
    print("Você errou! O seu chute foi menor que o número secreto.")
else:
    print("Você errou! O seu chute foi maior que o número secreto.")

print("Fim do jogo")