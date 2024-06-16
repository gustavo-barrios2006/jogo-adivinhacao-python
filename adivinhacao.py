print("* Bem vindo ao jogo de adivinhação *")
numero_secreto=42
chute=int(input("Digite seu chute"))
if(chute==numero_secreto):
    print("Você acertou!")
else:
    print("Você errou!")
print("Fim do jogo")