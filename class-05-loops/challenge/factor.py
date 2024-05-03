#Crie uma função que receba um número como parâmetro e calcule seu fatorial
def calc_fatorial(number):
  total =  1
  total *= number
  # while number > 0:
  #   total *= number
  #   number -= 1

  # for num in range(number, 1, -1):
  #   total *= num
  # return total

  # recursion
  if number == 1:
    return 1
  return number * calc_fatorial(number - 1)

try:
  number = int(input("Digite o número:"))
  result = calc_fatorial(number)

  print(f"O fatorial de {number} é {result}")
  
except ValueError:
  print("Somente inteiros!")
except RecursionError:
  print("Limite de recursão excedido!")