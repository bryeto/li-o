def calculadora():
    print("Escolha a operação:")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    
    operacao = input("Digite o número da operação desejada: ")
    
    if operacao in ['1', '2', '3', '4']:
        primeiro_valor = float(input("Digite o primeiro número: "))
        segundo_valor = float(input("Digite o segundo número: "))
        
        if operacao == '1':
            resultado = primeiro_valor + segundo_valor
        elif operacao == '2':
            resultado = primeiro_valor - segundo_valor
        elif operacao == '3':
            resultado = primeiro_valor * segundo_valor
        elif operacao == '4':
            if segundo_valor != 0:
                resultado = primeiro_valor / segundo_valor
            else:
                print("Erro! Não é possível dividir por zero.")
                return
        
        print(f"Resultado: {resultado}")
    else:
        print("Opção inválida. Tente novamente.")

calculadora()
