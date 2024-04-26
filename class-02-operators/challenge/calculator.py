# Capture dois números do usuário
# Faça as 4 operações(+, -, *, /) e atribua a  variaveis semanticas;
# Imprima na tela o valor das variáveis com sua operações

num1 = int(input("Digite o primeiro número:\n"))
num2 = int(input("Digite o segundo número:\n"))

sum = num1 + num2
sub = num1 - num2
mult = num1 * num2
div = num1 / num2

print(f"Soma = {sum}")
print(f"Subtração = {sub}")
print(f"Multiplicação = {mult}")
print(f"Divisão = {div:.2f}")

print(f"\033[0;33;44mDudu rei delas\033[0m")