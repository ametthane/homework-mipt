def calc(e):
    t = e.split()
    s = []
    for token in t:
        if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
            s.append(int(token))
        else:
            if len(s) < 2:
                return "Ошибка: недостаточно операндов для оператора " + token
            b = s.pop()
            a = s.pop()
            if token == '+':
                s.append(a + b)
            elif token == '-':
                s.append(a - b)
            elif token == '*':
                s.append(a * b)
            elif token == '/':
                if b == 0:
                    return "Ошибка: деление на ноль"
                s.append(a / b)
            else:
                return "Ошибка: неизвестный оператор " + token
    if len(s) != 1:
        return "Ошибка: некорректное выражение"
    return s[0]


expr = input()
print(calc(expr))

#Особая благодарность ИИ-модели Deepseek за помощь