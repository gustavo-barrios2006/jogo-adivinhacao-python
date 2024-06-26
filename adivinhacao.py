import random
print("* Bem vindo ao jogo de adivinhação *")
numero_secreto=random.randrange(1, 101)
print("Qual o nível de dificuldade?")
print("(1) Fácil (2) Médio (3) Difícil")
nivel=int(input("Defina o nível: "))
while(nivel<=0 or nivel>3):
    nivel=int(input("Nível inválido, digite um número de 1 a 3: "))
if(nivel==1):
    total_de_tentativas=20
elif(nivel==2):
    total_de_tentativas=10
else:
    total_de_tentativas=5
pontos=1000
for rodada in range(1, total_de_tentativas+1):
    print("Rodada {} de {}".format(rodada, total_de_tentativas))
    chute=int(input("Digite seu chute"))
    if(chute<1 or chute>100):
        print("Você deve digitar um número entre 1 e 100")
        continue
    if(chute==numero_secreto):
        print("Você acertou e fez {} pontos!".format(pontos))
        break
    elif chute<numero_secreto:
        print("Você errou! O seu chute foi menor que o número secreto.")
    else:
        print("Você errou! O seu chute foi maior que o número secreto.")
    pontos-=abs(chute-numero_secreto)
print("Fim do jogo")