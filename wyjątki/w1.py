def mnozenie(a, b):
    try:
        return a * b
    except TypeError:
        return "błędnie podane dane"

def mnozenie2(a, b):
    try:
        return int(a) * int(b)
    except Exception as e:
        return f"błędnie podano dane, wystąpił błąd: {e.args}"

def mnozenie3(a, b):
    try:
        return int(a) * int(b)
    except TypeError:
        return f"błędnie podano dane, wystąpił błąd: "
    except ValueError:
        return 0

# print(mnozenie(2, 2))
# print(mnozenie(2, "2"))
# print(mnozenie("2", "2"))
# print(mnozenie(5, 23)) # gdyby nie obsługiwać błędu to program by nie wykonał tej linijki

print(mnozenie2(3, 3))
print(mnozenie2(3, "3"))
print(mnozenie2("a", "b"))

print(mnozenie3(3, 3))
print(mnozenie3(3, "3"))
print(mnozenie3("a", "b"))
