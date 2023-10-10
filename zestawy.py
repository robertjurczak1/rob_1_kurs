primes = set()
primes.add(2)
primes.add(3)
primes.add(5)
print(primes)
primes.add(1)
primes.add(4)
print(primes)
primes.add(43)
primes.add(11)
primes.add(43)
print(primes)

names1 = {"Tomek", "Adam", "Krzysztof"}
names2 = {"Tomek", "Adam", "Jacek", "Tomek", "Andrzej"}

print(names1.difference(names2))
print(names2.difference(names1))
print(names1.intersection(names2)) # &
print(names1 | names2) # suma
print(names2.discard("adam"))

