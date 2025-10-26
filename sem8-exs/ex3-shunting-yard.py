def yard (exp):
    e = exp.replace(' ', '')
    t = []
    i = 0
    while i < len(e):
        if e[i] in '()+-*/':
            t.append(e[i])
            i += 1
        else:
            n = ''
            while i < len(e) and e[i].isdigit():
                n += e[i]
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
    return ' '.join(out)


expr = input()
print(f'Обратная польская запись: {yard(expr)}')
