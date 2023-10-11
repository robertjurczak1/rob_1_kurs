# f = open("tekst.txt", encoding="utf-8")
# text = f.read()
# print(text)
# f.close()
#
# f = open("baza.dat", "r")
# text = f.read(18)
# f.close()

# f = open("slice.dat", "w")
# f.write(text)

# f = open("slice.dat", "a")
# f.write(text)
# f.close()

with open("slice.dat", "r") as f:
    print(f.readline(7))
    print(f.readline())
    print(f.readline())

