# # sabendo que a média do colégio é 7, crie um programa que receba as notas do aluno e verifique se foi aprovado ou reprovado

def calc_avg(nota1, nota2):
  return (nota1 + nota2) / 2

try:
  nota1 = float(input("Digite a primeira nota: "))
  nota2 = float(input("Digite a segunda nota: "))
  
  if nota1 >= 0 or nota1 <= 10 or nota2 >= 0  or nota2 <= 10:
    raise Exception("Nota invalida!")

  avarage = round(calc_avg(nota1, nota2), 1)

  if avarage >= 7 and avarage <= 10:
    print("Aprovado com {avarage}") 
  elif avarage >= 0 and avarage < 7:
    print("Reprovado com  {avarage}")

except ValueError:
  print("Valor invalido!")
except Exception as error:
  print(error)
