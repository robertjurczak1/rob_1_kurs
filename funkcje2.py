def lista(x, items=[]):
    items.append(x)
    return items

while True:
    print("""Siemka!Wybierz opcję:
          1.😀 liczby
          2.😡 teksty
          3.😱 obojętnie co
    """)
    wynik = []
    opcja = int(input("Wybierz opcje (1-3)"))
    if opcja == 1:
        wybor = int(input("Jaką wstawić liczbę?:"))
        wynik = lista(wybor)
        print(wynik)
    elif opcja == 2:
        wybor = input("Jaki tekst wstawić do listy?:")
        wynik = lista(wybor)
        print(wynik)
    elif opcja == 3:
        wybor = input("co wstawić do listy?:")
        wynik = lista(wybor)
        print(wynik)
    elif opcja == 0:
        wynik.clear()
        break
    else:
        print("niepoprawny znak😡")
