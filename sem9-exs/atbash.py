class Atbash:
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

    def __init__(self):
        lowercase_code = {x: y for x, y in zip(self.alphabet, self.alphabet[::-1])}
        uppercase_code = {x.upper(): y.upper() for x, y in zip(self.alphabet, self.alphabet[::-1])}
        self._decode = lowercase_code
        self._decode.update(uppercase_code)

    def decode(self, text):
        return ''.join([self._decode.get(char, char) for char in text])


cipher = Atbash()
line = input()
while line != '.':
    print(cipher.decode(line))
    line = input()
