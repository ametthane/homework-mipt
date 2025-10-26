def calc(e):
    ex = e.replace(' ', '')
    t = []
    i = 0
    while i < len(ex):
        if ex[i] in '()+-*/':
            t.append(ex[i])
            i += 1
        else:
            n = ''
            while i < len(ex) and ex[i].isdigit():
                n += ex[i]
                i += 1
            t.append(n)


    def p(op):
        if op in ['+', '-']:
            return 1
        if op in ['*', '/']:
            return 2
        return 0
    out = []
    s = []
    for token in t:
        if token.isdigit():
            out.append(token)
        elif token == '(':
            s.append(token)
        elif token == ')':
            while s and s[-1] != '(':
                out.append(s.pop())
            s.pop()
        else:
            while (s and s[-1] != '(' and
                   p(s[-1]) >= p(token)):
                out.append(s.pop())
            s.append(token)
    while s:
        out.append(s.pop())
    print("Обратная польская запись:", ' '.join(out))


    def tp(tokens):
        if not tokens:
            return []
        mp = 100
        si = -1
        bc = 0
        for j in range(len(tokens) - 1, -1, -1):
            tok = tokens[j]
            if tok == ')':
                bc += 1
            elif tok == '(':
                bc -= 1
            elif bc == 0 and tok in '+-*/':
                cp = p(tok)
                if cp <= mp:
                    mp = cp
                    si = j
        if si != -1:
            op = tokens[si]
            l = tokens[:si]
            r = tokens[si + 1:]
            if len(l) > 1 and l[0] == '(' and l[-1] == ')':
                l = l[1:-1]
            if len(r) > 1 and r[0] == '(' and r[-1] == ')':
                r = r[1:-1]
            return [op] + tp(l) + tp(r)
        else:
            if len(tokens) > 1 and tokens[0] == '(' and tokens[-1] == ')':
                return tp(tokens[1:-1])
            return tokens
    pr = tp(t)
    print("Прямая польская запись:", ' '.join(pr))


expr = input()
calc(expr)

#Особая благодарность ИИ-модели Deepseek за помощь