s = input()
count = 0
if len(s) > 4:
    for i in range(4):
        if s[i].isupper():
            count += 1
else:
    for i in range(len(s)):
        if s[i].isupper():
            count += 1
if count >= 3:
    print(s.upper())
else:
    print(s)

