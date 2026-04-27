users = [
    [100, 499, 30],
    [250, 999, 90],
    [50, 199, 10]
]

print(len(users))        # rows
print(len(users[0]))     # columns

# Extract one feature
for user in users:
    print(user[0])

