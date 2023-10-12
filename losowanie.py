import random

k6 = random.randint(1, 6) # tutaj jest od 1 do 6
print("wynik rzutu kością: ", k6)

lista = ["Tomek", "Ania", "Mikołaj", "Albert"]
loteria = random.choice(lista)
print("Elektryczną Izerę wygrywa: ", loteria)

liczba = random.random()
print(liczba)
print(liczba*100)