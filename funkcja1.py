def nicCiekawego():
    pass

def ksero():
    return "kopiuje"

def ksero_kolorowe(ilosc: int):
    return "kopiuje " * ilosc

def ksero_mono(ilosc: int, tekst: str):
    return tekst * ilosc

def ksero_mono_dom(tekst: str, ilosc=1):
    return tekst * ilosc

def ksero_mono_dom_duo(tekst="duo ", ilosc=1):
    return tekst * ilosc

print(nicCiekawego())
print(ksero())
print(ksero_kolorowe(4))
print(ksero_mono(4, "robert "))
print(ksero_mono("robert ", 6))
print(ksero_mono_dom("dom ", 2))
print(ksero_mono_dom("chatka ", ))
print(ksero_mono_dom_duo(ilosc=5))