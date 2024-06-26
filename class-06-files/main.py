# "r" - read
# "w" - write
# "r+" - read/write
# "x" - create
# "a" - append
try:
  films = open("class-06-files/films.txt", "r", encoding="utf-8")

  print(films.read())
  films.close()
except FileNotFoundError:
  print("Arquivo não encontrado!")


try:
  with open("class-06-files/files/films.txt", "r+", encoding="utf-8") as list_films:
    print(list_films.read())
    print(list_films.tell())
    list_films.write("Piratas do Caribe\n")
    list_films.seek(0)
    print(list_films.readlines())

    for film in list_films:
      print(film.upper())

except FileNotFoundError:
  print("Arquivo não encontrado!")