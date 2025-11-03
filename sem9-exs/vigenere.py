class Vigenere:
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    frequencies = {
        'о': 33, 'е': 32, 'а': 31, 'и': 30, 'н': 29,
        'т': 28, 'с': 27, 'р': 26, 'в': 25, 'л': 24,
        'к': 23, 'м': 22, 'д': 21, 'п': 20, 'у': 19,
        'я': 18, 'ы': 17, 'ь': 16, 'г': 15, 'з': 14,
        'б': 13, 'ч': 12, 'й': 11, 'х': 10, 'ж': 9,
        'ш': 8, 'ю': 7, 'ц': 6, 'щ': 5, 'э': 4,
        'ф': 3, 'ъ': 2, 'ё': 1
    }

    def __init__(self, keyword=None):
        self.alphaindex = {ch: idx for idx, ch in enumerate(self.alphabet)}
        if keyword:
            self.key = [self.alphaindex[ch] for ch in keyword.lower()
                        if ch in self.alphaindex]
        else:
            self.key = None

    def caesar(self, letter, shift):
        if letter in self.alphaindex:  # строчная буква
            index = (self.alphaindex[letter] - shift) % len(self.alphabet)
            return self.alphabet[index]
        elif letter.lower() in self.alphaindex:  # заглавная буква
            return self.caesar(letter.lower(), shift).upper()
        else:
            return letter

    def encode(self, line):
        ciphertext = []
        key_pos = 0
        for ch in line:
            if ch.lower() in self.alphaindex:
                shift = self.key[key_pos % len(self.key)]
                cipherletter = self.caesar(ch, -shift)
                ciphertext.append(cipherletter)
                key_pos += 1
            else:
                ciphertext.append(ch)
        return ''.join(ciphertext)

    def decode(self, line):
        plaintext = []
        key_pos = 0
        for ch in line:
            if ch.lower() in self.alphaindex:
                shift = self.key[key_pos % len(self.key)]
                plainletter = self.caesar(ch, shift)
                plaintext.append(plainletter)
                key_pos += 1
            else:
                plaintext.append(ch)
        return ''.join(plaintext)

    def text_to_indices(self, text):
        return [self.alphaindex[c] for c in text.lower()
                if c in self.alphaindex]

    def indices_to_text(self, indices):
        return ''.join(self.alphabet[i] for i in indices)

    def frequency_analysis(self, group):
        alphabet_size = len(self.alphabet)
        best_shift = 0
        best_score = -1
        group_freq = [0] * alphabet_size
        for idx in group:
            group_freq[idx] += 1
        total = len(group)
        if total > 0:
            group_freq = [f / total for f in group_freq]
        for shift in range(alphabet_size):
            score = 0
            for i in range(alphabet_size):
                shifted_idx = (i + shift) % alphabet_size
                score += (self.frequencies.get(self.alphabet[i], 0)
                          * group_freq[shifted_idx])
            if score > best_score:
                best_score = score
                best_shift = shift
        return best_shift

    def find_key(self, ciphertext, key_length=8):
        clean_text = ''.join(c for c in ciphertext.lower()
                             if c in self.alphaindex)
        groups = [[] for _ in range(key_length)]
        for i, ch in enumerate(clean_text):
            groups[i % key_length].append(self.alphaindex[ch])
        key_indices = [self.frequency_analysis(group) for group in groups]
        return self.indices_to_text(key_indices)

    def auto_decrypt(self, ciphertext, key_length=8):
        found_key = self.find_key(ciphertext, key_length)
        print(f"Найденный ключ: {found_key}")
        self.key = [self.alphaindex[ch] for ch in found_key]
        return self.decode(ciphertext)


if __name__ == '__main__':
    print("Введите зашифрованный текст "
          "(введите '.' на отдельной строке для окончания ввода):")
    lines = []
    while True:
        try:
            s = input()
        except EOFError:
            break
        if s == '.':
            break
        lines.append(s)
    ciphertext = '\n'.join(lines)
    v = Vigenere()
    # можно изменить длину ключа (для ноутбука ключ "мфти")
    decrypted = v.auto_decrypt(ciphertext, key_length=4)
    print("\nРасшифрованный текст:\n")
    print(decrypted)

# Особая благодарность моему дорогому товарищу Chat GPT за то что не дал мне сойти с ума
