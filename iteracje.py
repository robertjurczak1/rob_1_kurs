from datetime import date, timedelta

tablica = [1, 2, 3, 4, 5, 6, 7, 8, 9]

#for i in tablica:
 #   print(f"2 do potęgi {i} to {2 ** i}")

# for i in range(1, 10):
#     print(f"2 do potęgi {i} to {2 ** i}")
#     print("test")
#     for j in range(1, 5):
#         print("a ja sobie działam w pętli 2")
# print("to też test")

# nieskończona pętla przypadkiem
# names = ["Tomek", "Marek", "Anna", "Jacek"]
# for name in names:
#     if name.istitle():
#         names.append(name.upper())
# print("zmodyfikowana lista", names)

cyfry = []
# while True:
#     print("podaj cyfry, lub '0' aby zakończyć")
#     cyfra = int(input("podaj cyfrę"))
#
#     if cyfra == 0:
#         break
#     elif cyfra > 100:
#         print("podałeś dużą cyfrę!")
#     elif cyfra < 0:
#         print("podałeś cyfrę ujemną")
#     else:
#         cyfry.append(cyfra)
#
# print("Lista cyfr:", cyfry)

# licznik = 0
# while licznik < 5:
#     print("Stan licznika:", licznik)
#     licznik += 1 # licznik = licznik + 1

# people = ["Tomek", "Anna", "Jacek", "Andrzej"]
# ages = [23, 24, 22, 21]
# position = 0
# while position < len(people):
#     person = people[position]
#     age = ages[position]
#     print(person, age)
#     position += 1

today = date.today()
tomorrow = today + timedelta(days=1)
products = [
    {"id": "1", "exp_date": today, "price": 10.0},
    {"id": "2", "exp_date": tomorrow, "price": 20.0},
    {"id": "3", "exp_date": today, "price": 50.0},
]
for product in products:
    if product["exp_date"] != today:
        continue
    product["price"] *= 0.8
    print("Cena dla id", product["id"])
    print("wynosi", product["price"])
