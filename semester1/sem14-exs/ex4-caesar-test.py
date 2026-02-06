import unittest


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


class TestCaesarGeneral(unittest.TestCase):

    def test_inverse_property(self):
        k = 17
        cipher = Caesar(k)
        inv_cipher = Caesar(-k)
        testt = "обратимое преобразование"
        encoded = cipher.decode(testt)
        decoded = inv_cipher.decode(encoded)
        self.assertEqual(decoded, testt)

    def test_preserve_non_alphabet_chars(self):
        cipher = Caesar(10)
        testt = "123 !@# test Тест"
        res = cipher.decode(testt)
        for or_char, res_char in zip(testt, res):
            if or_char.lower() not in Caesar.alphabet:
                self.assertEqual(res_char, or_char)

    def test_case_preservation(self):
        cipher = Caesar(8)
        ttm = "ТеСт С РеГиСтРоМ"
        resm = cipher.decode(ttm)
        for i, char in enumerate(ttm):
            if char.isupper():
                self.assertTrue(resm[i].isupper())
            elif char.islower():
                self.assertTrue(resm[i].islower())


key = int(input('Введите ключ: '))  # 14 для задания
cipher = Caesar(key)
line = input()
while line != '.':
    print(cipher.decode(line))
    line = input()
