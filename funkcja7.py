def print_the_next_number(start):
    print(start + 1)
    if start >= 10:
        return "idź na kawę"
    return print_the_next_number(start+1)

print(print_the_next_number(5))

# funkcja odliczania

def count_down(n):

    print(n - 1)
    if n == 1:
        return "start"
    return count_down(n-1)

print(count_down(10))

def countdown(n):
    if n == 0:
        print("lift")
    else:
        print(n)
        return countdown(n-1)

countdown(3)