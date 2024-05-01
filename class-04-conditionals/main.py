age = 18
cnh = True

if (age >= 18):
  print("Maior de Idade")
else: 
  print("Menor de idade")

if age >= 18 and cnh:
  print("Maior de Idade, vc já pode dirigir")
else: 
  print("Menor de idade, vc não pode dirigir")

if age >= 18 and age <= 70:
  print("Voto obrigatorio!")
elif age < 16:
  print("Não pode votar!")
else:
  print("Voto facultativo!")

# print(2/0)
try:
  print(2/2)
except TypeError:
  print("Formato invalido!")
except ZeroDivisionError:
  print("Não pode dividir por zero!")
except:
  print("Error")
finally:
  print("Fim da requisição!")

print("Running...")