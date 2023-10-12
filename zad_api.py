import requests

miasto = input("Podaj miasto: ") # jeżeli chcemy wprowadzić dowolne miasto to dodaliśmy. wprowadziliśmy zamiast kielce {miasto} i f przed adresem
url = requests.get(f"http://api.weatherapi.com/v1/current.json?key=d863af85e8fa43618f682810220812&q={miasto}&aqi=no")
print(url.status_code)
lokalizacja = url.json()["location"]["name"]
print(lokalizacja)
temperatura = url.json()["current"]["temp_c"]
print(temperatura)

with open("pogoda.txt", "a", encoding="utf-8") as f: # zmieniliśmy z w na a
    f.write(f"\nW mieście {lokalizacja} jest {temperatura} stopni C") # dodaliśmy \n a w pliku pojawiło się w nowej linijce