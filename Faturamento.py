# criando vetor e inicializando variaveis
fat = [550, 600, 768, 450.50, 342.7, 700.8, 245, 678.9, 532.4, 890.5]
maior = menor = 0
diaMaior = diaMenor = 0
media = sum(fat) / 10
numDia = 0

# realizando calculos e atribuindo valores
for i in range(0, len(fat), 1):
    if fat[i] > media:
        numDia += 1
    if i == 0:
        maior = fat[0]
        menor = fat[0]
        diaMaior = diaMenor = i + 1
    else:
        if fat[i] > maior:
            maior = fat[i]
            diaMaior = i + 1
        if fat[i] < menor:
            menor = fat[i]
            diaMenor = i + 1

# retorno
print(f'O maior faturamento foi R${maior:.2f} e ocorreu no dia {diaMaior}.')
print(f'O menor faturamento foi R${menor:.2f} e ocorreu no dia {diaMenor}.')
print(f'O número de dias em que o faturamento foi maior que a média é {numDia}.')
