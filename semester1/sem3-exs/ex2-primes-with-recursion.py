import math

def isprime(x):
    if x < 2:
        return False
    if x == 2:
        return True
    for i in range(2, int(math.sqrt(x)+1)):
        if x % i == 0:
            return False
    return True


def decompose(x, i=2):
    if x == 1:
        return []
    if isprime(i) == True and x % i == 0:
        return [i] + decompose(x//i, i)
    return decompose(x, i+1)


n = int(input())
print(" * ".join(map(str, decompose(n))))


