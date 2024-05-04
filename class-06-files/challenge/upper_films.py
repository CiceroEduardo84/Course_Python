# Abra o sarquivos de filmes e crie um array
# Passe os nomes do array para caixa alta
# Escreva (write) os nomes em um novo arquivo
try:
  with open("class-06-files/files/films.txt", "r", encoding="utf-8") as list_films,\
       open("class-06-files/files/upper_films.txt", "w", encoding="utf-8") as upper_films:
    
    for film in list_films:
      upper_films.write(film.upper())
except FileNotFoundError:
  print("Arquivo não encontrado!")