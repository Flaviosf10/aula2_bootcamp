# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.

import math

raio = float(input('Digite o raio do circulo: '))
area = (math.pi * (raio ** 2))
print (f'A área do circulo é: {area:,.2f}')
