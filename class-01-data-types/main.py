milk = "Leite instegral"
milk = "Leite desnatado"
volume = 2

print(type(milk))
print(type(volume))

preparation = volume + 1
preparation2 =  milk + str(volume) 

print(preparation2)

life_cat =  str(volume + 5)
print("O gato bebe " + milk )
print("E tem " + life_cat + " vidas")

print("O gato bebe " + milk + " e tem " + life_cat + " vidas" )
print(f"O gato bebe {milk} e tem {life_cat} vidas")