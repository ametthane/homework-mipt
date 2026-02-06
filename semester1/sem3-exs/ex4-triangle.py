def triangle(size, symb, i=1):
    if i > (size//2)+1:
        return
    print(symb*i)
    triangle(size, symb, i+1)
    if i != (size//2)+1:
        print(symb*i)

s, sy = input().split()
triangle(int(s), sy)