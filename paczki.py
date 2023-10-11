import json

with open("trening.json", "r") as f:
    data = json.load(f) # funkcja ładuje z pliku


paczek1 = data["batters"] ["batter"][2]["type"]
print(paczek1)

paczek2 = data["topping"][4]["type"]
print(paczek2)