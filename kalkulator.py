def dodawanie(a, b):
    return a + b

def odejmowanie(a, b):
    return a - b

def mnozenie(a, b):
    return a * b

while True:
    print("""Witamy w domowym kalkulatorze. Jakie działanie chcesz wykonać:
          1.Dodawanie
          2.Odejmowanie
          3.Mnożenie
    """)

    opcja = int(input("Wybierz opcje (1-3)"))
    if opcja == 1:
        wybora = int(input("Jakie liczby chcesz dodać (a)?:"))
        wyborb = int(input("Jakie liczby chcesz dodać (b)?:"))
        wynik = dodawanie(wybora, wyborb)
        print("a➕b = ", wynik)
        print("świetnie liczysz!")
    elif opcja == 2:
        wybora = int(input("Jakie liczby chcesz odejmować (a)?:"))
        wyborb = int(input("Jakie liczby chcesz odejmować (b)?:"))
        wynik = odejmowanie(wybora, wyborb)
        print(wynik)
    elif opcja == 3:
        wybora = int(input("Jakie liczby chcesz mnożyć (a)?:"))
        wyborb = int(input("Jakie liczby chcesz mnożyć (b)?:"))
        wynik = mnozenie(wybora, wyborb)
        print("a❌b = ", wynik)
    elif opcja == 0:
        break
    else:
        print("niepoprawne działanie")