lista = []
lista.append("robert")
print(lista)
lista.append(456)
print(lista)
lista.append(("a", "b", "c"))
print(lista)
print(lista[0])
print(lista[2])
print(lista[2][0])
tekst = "hello"
print(list(tekst))
liczby = [2, 3, 4]
nowe_liczby = [x + 4 for x in liczby]
print(nowe_liczby)
liczby.sort(reverse=True)
print(liczby)
liczby.insert(2, 248)
print(liczby)
liczby[2] = "robert"
print(liczby)
liczby.pop(2)
print(liczby)
liczby.remove(3)
print(liczby)