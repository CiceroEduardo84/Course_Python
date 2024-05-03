#Loops

print("Start")

# while true:
  # print("loop")

count = 0
while count < 10:
  count += 1
  print(count)
  
musics = ["Time", "Bateu 20h", "Clocks", "Menina Veneno", "Morango do Nordeste", "Boate Azul"]

index_music = 0
while index_music < len(musics):
  print(musics[index_music])
  index_music += 1

for i in range(0, 10, 2):
  print(i)

for music in musics:
  print(music)

letters = [
  ["A", "B", "C"],
  ["A", "B", "C"],
]

for array in letters:
  for letters in array:
    print(letters)

print("End")