import re

tekst = "Python to nie tylko gad, ale także język programowania"
# wynik = re.match(r"Python", tekst) match wyszukuje tylko pierwsze znaki
# print(wynik)
# print(f"Dopasowano: {wynik.group()}, początek: {wynik.span()[0]}, koniec: {wynik.span()[1]}")
# print(f"Dopasowano: {wynik.group()}, początek: {wynik.start()}, koniec: {wynik.end()}")

wzorzec = re.compile(r"ni")
# wynik = wzorzec.search(tekst) wyłącczono
wynik = wzorzec.finditer(tekst)
lista_wyn = list(wynik)
print(type(wynik))

# wynik = re.search(r"nie", tekst)
print(wynik)
# print(f"Dopasowano: {wynik.group()}, początek: {wynik.span()[0]}, koniec: {wynik.span()[1]}")
# if wynik:
#     print(f"Dopasowano: {wynik.group()}, początek: {wynik.start()}, koniec: {wynik.end()}")
# else:
#     print(wynik)

if len(lista_wyn) > 0:
    # print(f"Dopasowano: {wynik.group()}, początek: {wynik.start()}, koniec: {wynik.end()}")
    print(f"dopasowano: {len(lista_wyn)}")
    for w in lista_wyn:
        print(f"dopasowano: {w.group()}, początek: {w.start()}, koniec: {w.end()}")
else:
    print(wynik)
print(re.split(r" ", tekst))

wzorzec2 = re.compile(r".+?")
print(wzorzec2.findall(tekst)) # rozbijanie na pojedyncze litery

# https://miroslawmamczur.pl/wyrazenia-regularne-czym-sa-i-jak-pisac-wlasne-regexy/

