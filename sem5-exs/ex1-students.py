stud = input().split("student_")
stud.remove("")
students = []
for i in stud:
    num = i[:3]
    score = int(i[3:])
    students.append((num, score))
max_sc = -1
for num, score in students:
    if score > max_sc:
        max_sc = score
res = []
for num, score in students:
    if score == max_sc:
        res.append(num)
print('-'.join(res))

