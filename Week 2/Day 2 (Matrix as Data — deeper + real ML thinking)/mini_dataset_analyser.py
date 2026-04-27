students = [
    [85, 90, 78],
    [70, 60, 65],
    [95, 88, 92]
]


# Print each student
for s in students:
    print(s)

for s in students:
    avg = sum(s) / len(s)
    print(avg)

math_total = 0
science_total = 0
english_total = 0

for s in students:
    math_total += s[0]
    science_total += s[1]
    english_total += s[2]

print(math_total / len(students))
print(science_total / len(students))
print(english_total / len(students))