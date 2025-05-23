def encontrar_maior(valor_a, valor_b):
    return max(valor_a, valor_b)

def eh_multiplo(numero_base, numero_verificacao):
    return numero_base % numero_verificacao == 0

def calcular_area_quadrado(tamanho_lado):
    return tamanho_lado ** 2

def calcular_area_triangulo(comprimento_base, altura_triangulo):
    return (comprimento_base * altura_triangulo) / 2

print(encontrar_maior(10, 20))  # 20
print(eh_multiplo(10, 2))  # True
print(calcular_area_quadrado(5))  # 25
print(calcular_area_triangulo(6, 4))  # 12.0
