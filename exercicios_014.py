# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.

data_digitada = input(" Digite uma data no formato DD/MM/AAAA: ")
data_dividida = data_digitada.split("/")
print(f"Voçê nasceu no dia: {data_dividida[0]},")
print(f"Voçê nasceu no mês: {data_dividida[1]},")
print(f"Voçê nasceu no ano de: {data_dividida[2]},")