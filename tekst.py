wiek = 2023 - 1978

str1 = 'to jest tekst 1\n'
str2 = f"wiek = {wiek}\n"
str3 = f"""to jest też wiek {wiek},
          ale ma specjalne opcje
          i tu kolejny tekst"""

print(str1, str2, str3)

tekst = "Kurs Python"
print(tekst.lower())
print(tekst.count("r"))
print(len(tekst))
print(tekst[5])
print(tekst[0:3])
print(tekst[0:3]+"a")
print(tekst[0:4]+"y")
print(tekst[:4])
print(tekst[1:])
print(tekst[1:10:2])
print(tekst[1::2])

stary_format = "Hello %s!"
print(stary_format % "Robert")

sredni_format = "Hello {}!"
print(sredni_format.format("Robert"))

print(str1, "tu jakiś tekst...", str2)
