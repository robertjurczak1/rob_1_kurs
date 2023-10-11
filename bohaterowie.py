import json

with open("heroes.json", "r") as f:
    data = json.load(f) # funkcja ładuje z pliku

# print(data)
odczyt1 = data["secretBase"]
odczyt2 = data["members"][0]["powers"][2]
odczyt3 = data["members"][0]["powers"]
print(odczyt2[2:4])
lista = []
for index, wartosc in enumerate(data["members"]):
    print(index, wartosc)