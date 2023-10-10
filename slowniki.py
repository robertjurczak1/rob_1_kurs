slownik = {"a1": 1999}
print(slownik["a1"])
slownik["a2"] = 4532
print(slownik)
slownik["a1"] = 9876
print(slownik)
print(slownik.get("a1"))
slownik["a3"] = [5, 6, 7]
print(slownik)
print(slownik["a3"][1])

