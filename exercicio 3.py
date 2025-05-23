import math

def dobrar_valor(valor):
    print(f"O dobro de {valor} é {valor * 2}")

def calcular_comprimento_circunferencia(raio_circulo):
    return 2 * math.pi * raio_circulo

def unir_textos(texto1, texto2):
    return f"{texto1} {texto2}"

dobrar_valor(5)
print(f"O comprimento da circunferência com raio 3 é {calcular_comprimento_circunferencia(3):.2f}")
print(unir_textos("Olá", "Mundo"))
