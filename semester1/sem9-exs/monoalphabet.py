class Monoalphabet:
    alphabet = "оеаинтсрвлкмдпуяыьгзбчйхжшюцщэфъё"

    def __init__(self, keytable):
        lowercase_code = {x: y for x, y in zip(self.alphabet, keytable)}
        uppercase_code = {x.upper(): y.upper() for x, y
                          in zip(self.alphabet, keytable)}
        self._decode = lowercase_code
        self._decode.update(uppercase_code)

    def decode(self, text):
        return ''.join([self._decode.get(char, char) for char in text])


k = "вшпяжумгхчэдёфълйбиыткзьрсноеающц"  # для задания
cipher = Monoalphabet(k)
line = input()
while line != '.':
    print(cipher.decode(line))
    line = input()
