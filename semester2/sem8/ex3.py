def solve(s1, s2):
    return s1[1] + s1[0] + s1[2:] + '-' + s2


st1 = input()
st2 = input()
print(solve(st1, st2))
