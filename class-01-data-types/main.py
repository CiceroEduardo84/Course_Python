#Primitive Types

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

name = "Eduardo"
age = 31

is_admin = True #boolean: True or False

print(is_admin)
print(type(is_admin))

# Structural Types(Collections)

animes = ["Dragon ball", "Naruto", "Jojo", "Death Note"]
              # =>  0          1         2       3
              # <= -4         -3        -2      -1
print(animes)
print(type(animes))
print(animes[0])
print(animes[3])
print(animes[-1])

list = ["A", 123, True, ["B", "C"]]

print(list[0])
print(list[3])
print(list[-1])
print(list[3][0])

list[2] = False
list[-1][0] = "D" 
print(list)
print(len(list)) #length

# Tuple
tuple = ("A", 123, True)
print(type(tuple))
print(tuple[0])

# tuple[1] = 789 #tuple is immutable
print(tuple)

# Dict
dict = {
  "name":"Arthur", 
  "age": 31,
  "is_admin": is_admin,
}
print(type(dict))
print(dict)
print(dict["name"])
print(dict["is_admin"])
print(dict["age"])