
# x = "Renan"
# y = "Straquicini"
# print(x, y)

num1 = float(input("Digite o primeiro valor: "))
num2 = float(input("Digite o segundo valor: "))
soma = num1 + num2
media = (num1 + num2) / 2

# a, b, c = "R", "G", "B"
# print(a, b, c)

# print("A soma de ", str(num1), " com ", str(num2), " é igual a ", str(soma))
# print("A soma de " + str(num1) + " com " + str(num2) + " é igual a " + str(soma))
# fstring
print(f'A soma de {num1} com {num2} é igual a {soma:.2f}')
print(f'A soma de {num1} com {num2} é igual a {media:.2f}')