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


def decompose(x):
    ans = []
    while x > 1:
        for i in range(1, int(x+1)):
            if isprime(i) == True and x % i == 0:
                ans.append(i)
                x = x/i
    return " * ".join(str(j) for j in ans)


n = int(input())
print(decompose(n))


