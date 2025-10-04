s = input()
if len(s) <= 2:
    print(ord(s[0]))
elif 2 < len(s) < 10:
    ans = ord(s[0]) + ord(s[(len(s)-1)//2]) + ord(s[len(s)-1])
    print(ans)
else:
    print(ord(s[len(s)-1]))