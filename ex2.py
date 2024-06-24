import random

def jogo():
    num_aleatorio = random.randint(0, 50)
    i = 0
    acert_num = " "
    while i < 5:
        acert_num = int(input("Tente acertar o número que o computador escolheu. Esse número é vai de 0 a 50: "))
        i+=1
        if acert_num == num_aleatorio and i == 1:
            print(f"Parabéns, você acertou o número, que foi de {acert_num}")
            print("Você conseguiu 100 pontos!")
        elif acert_num == num_aleatorio and i == 2:
            print(f"Parabéns, você acertou o número, que foi de {acert_num}")
            print("Você conseguiu 50 pontos!")
        elif acert_num == num_aleatorio and i == 3:
            print(f"Parabéns, você acertou o número, que foi de {acert_num}")
            print("Você conseguiu 30 pontos!")
        elif acert_num == num_aleatorio and i == 4:
            print(f"Parabéns, você acertou o número, que foi de {acert_num}")
            print("Você conseguiu 20 pontos!")
        elif acert_num == num_aleatorio and i == 5:
            print(f"Parabéns, você acertou o número, que foi de {acert_num}")
            print("Você conseguiu 10 pontos!")
        elif acert_num > 50 or acert_num < 0:
            print("Por favor, comece o jogo novamente e insira um número que está no intervalo permitido (números de 0 a 50)! ")
            break
        else:
            print("Tente denovo!")
jogo()

jogar_novamente = " "

while True:
    jogar_novamente = input("Deseja jogar? Digite 's' para sim, e 'n' para não: " )
    if jogar_novamente == "s":
        jogo()
    elif jogar_novamente == "n":
        print("Finalizando o programa")
        break





