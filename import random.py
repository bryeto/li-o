import random

def jogo_par_ou_impar():
    escolha = input("Você quer ser par ou ímpar? (par/impar): ").strip().lower()
    
    while escolha not in ["par", "impar"]:
        escolha = input("Escolha inválida. Digite 'par' ou 'impar': ").strip().lower()

    numero_jogador = int(input("Escolha um número entre 0 e 9: "))
    numero_pc = random.randint(0, 9)
    
    soma = numero_jogador + numero_pc
    resultado = "par" if soma % 2 == 0 else "impar"
    
    print(f"\nVocê escolheu {numero_jogador}, o computador escolheu {numero_pc}. A soma é {soma}, que é {resultado}.")

    if resultado == escolha:
        print("Parabéns, você venceu!")
    else:
        print("Que pena, o computador venceu!")

jogo_par_ou_impar()

