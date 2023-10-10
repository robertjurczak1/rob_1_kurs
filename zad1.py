"""
chcemy stwierdzić, czy co najmniej jeden element na liście ma wynik True (czyli jest w typie bool)
zadbaj o wyświetlenie wyników. dopisz po ilu iteracjach odnalazł się true
"""

items = [0, None, 0.0, True, 0, 7]

# licz = 0
# for item in items:
#     if type(item) == bool:
#         print("znalazłem typ bool")
#         break
#     licz += 1
# print("Po ilu iteracjach odnalazło się True:", licz)

# while True
#     if type(item) == bool:

licznik = 0
found = None
for i in items:
    print("skanuje itemy...", i)
    licznik += 1
    if i:
        found = True
        break
if found:
    print("Znalazłem TRUE!")
print("na pozycji", licznik)


