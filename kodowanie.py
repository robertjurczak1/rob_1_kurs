a = "Helló"
b = a.encode("utf-8")
print(b)
print(a)
print(b.decode("utf-8"))

x = 123.456
y = 1234.456

print(format(x, "0.2f"))
print(format(x, "0.1f"))
print(format(x, "6.1f"))
print(format(y, "6.1f"))
print(format(y, "*<10.2f")) # wypełnia *

napis = "Tomek"
print(format(napis, "<10"))
print(format(napis, "-<10"))

name = "IBM"
shares = 50
price = 549.10

r = "{:>10s} {:10d} {:10.2f}".format(name, shares, price)
print(r)

import os
import pathlib as path

# names = os.listdir("venv/bin")
# for name in names:
#     print(name)

for filename in path.Path("").glob("*.txt"):
    print(filename)

def countdown2(n):
    while n > 0:
        yield print(f"T-minus {n}\n")
        n -= 1
    yield print("Start!\n")

for x in countdown2(5):
    pass

def counter(start=0):
    n = start
    while True:
        result = yield n
        print(n)

        if n == 100:
            break
        if result == "q":
            break
        n += 1

c = counter()
next(c)
print("coś tu innego robię")
print(next(c))
print(next(c))
print("coś tu innego robię")
print("coś tu innego robię")
print(next(c))

for _ in counter(5):
    pass

next(c)
next(c)
c.send("q") # operacja specjalna
next(c)
next(c)




