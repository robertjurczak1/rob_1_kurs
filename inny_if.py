x = [1, 2]

match x:
    case[]:
        print("pusta lista")
    case[1]:
        print("lista z 1 elementem", x)
    case[1, 2]:
        print("lista z 2 elementem", x)
    case[1, 2, 3]:
        print("lista z 3 elementem", x)
    case _:
        print("inny przypadek...")

if x== []:
# if not x:
    print("pusta liczba")
elif x == [1]:
    print("lista z 1 elementem o wartości 1")
elif x == [1, 2]:
    print("lista z 2 elementem o wartości 1 i 2")
elif x == [1, 2, 3]:
    print("lista z 3 elementem o wartości 1, 2 i 3")
else:
    print("inny lista...")