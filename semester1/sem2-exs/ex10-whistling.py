vow = 'аеёиоуыэюя'


def translate(word):
    res = []
    i = 0
    while i < len(word):
        if word[i] in vow:
            begin = i
            while i < len(word) and word[i] in vow:
                i += 1
            row = word[begin:i]
            if len(row) == 1:
                res.append(row)
                res.append('с' + row)
            else:
                res.append(row[0])
                if begin > 0 and word[begin - 1] not in vow:
                    res.append('с' + row[0])
                for j in range(1, len(row)):
                    res.append(row[j])
        else:
            res.append(word[i])
            i += 1
    return ''.join(res)


with open(r'input.txt', 'r', encoding='utf-8') as inp:
    s = inp.read().strip().split()
ans = [translate(word) for word in s]
with open(r'output.txt', 'w', encoding='utf-8') as outp:
    outp.write(' '.join(ans))

# Особая благодарность ИИ-модели Deepseek за помощь с реализацией идеи