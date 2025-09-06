def to_any_base (num, base):
    if num == 0:
        return "0"
    dig = "0123456789"
    res = ""
    while num > 0:
        res = dig[num % base] + res
        num //= base
    return res


N = input("Введите число N: ")
b = int(input("Введите  основание системы счисления N: "))
c = int(input("Введите  основание системы счисления, в которую хотите перевести N: "))
N = int(N, b)
if c == 10:
    print("Ответ: ", N)
else:
    print("Ответ: ", to_any_base(N, c))

# Выражаю особую благодарность ИИ-помощнику Google Gemini
