def product(first: int, *args): -> int #kolejny element informacyjny - -> int, podobnie jak first: int
    result = first
    for x in args:
        result = result * x
    return result

print(product(10))
print(product(10, 20))
print(product(10, 2, 4, 6))

def make_table(**kwargs):
    """Funkcja wypisuje tabela z danymi osobowymi"""
    for key, value in kwargs.items():
        print(f"{key} = {value}")

make_table(name="Jan", surname="Kowalski", age=32)
make_table(name="Anna", surname="Nowak", age=32, city="Poznań")