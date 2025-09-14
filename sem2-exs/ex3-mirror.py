s = input()
is_pal = s == s[::-1]
mir_dict = {
    'A': 'A', 'H': 'H', 'I': 'I', 'M': 'M', 'O': 'O', 'T': 'T',
    'U': 'U', 'V': 'V', 'W': 'W', 'X': 'X', 'Y': 'Y', '1': '1',
    '8': '8', 'E': '3', '3': 'E', 'J': 'L', 'L': 'J', 'S': '2',
    '2': 'S', 'Z': '5', '5': 'Z'
}
is_mir = True
m = []
for c in s:
    if c not in mir_dict:
        is_mir = False
        break
    m.append(mir_dict[c])
m_str = ''.join(m)
if m_str != s[::-1]:
    is_mir = False
if not is_pal and not is_mir:
    print(f"{s} is not a palindrome")
if not is_pal and is_mir:
    print(f"{s} is a mirrored string")
if is_pal and not is_mir:
    print(f"{s} is a regular palindrome")
if is_pal and is_mir:
    print(f"{s} is a mirrored palindrome ")

# Особая благодарность ии-модели Deepseek за помощь с идеей