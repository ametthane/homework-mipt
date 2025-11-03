class Caesar:
    alphabet = "яюэьыъщшчцхфутсрпонмлкйизжёедгвба"

    def __init__(self, k):
        self._decode = dict()
        for i in range(len(self.alphabet)):
            letter = self.alphabet[i]
            decoded = self.alphabet[(i - k) % len(self.alphabet)]
            self._decode[letter] = decoded
            self._decode[letter.upper()] = decoded.upper()

    def decode(self, text):
        return ''.join([self._decode.get(char, char) for char in text])


key = int(input('Введите ключ: '))  # 14 для задания
cipher = Caesar(key)
line = input()
while line != '.':
    print(cipher.decode(line))
    line = input()
