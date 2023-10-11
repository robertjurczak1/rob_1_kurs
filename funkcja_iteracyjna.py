def sum_first(n):
    result = 0
    for i in range(n):
        result += i + i
    return result

def prime(x):
    for i in range(2, x):
        if (x % i) == 0:
            return False
        return True

print(sum_first(5))
print(prime(5))