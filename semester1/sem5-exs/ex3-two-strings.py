def swap(s):
    chars = list(s)
    chars[0], chars[1] = chars[1], chars[0]
    return "".join(chars)


strs = input().split(" ")
str1 = str(strs[0])
str2 = str(strs[1])
print(f'{swap(str1)}-{swap(str2)}')