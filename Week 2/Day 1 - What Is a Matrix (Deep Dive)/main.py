matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

print(matrix)

print(matrix[0])      # first row
print(matrix[1])      # second row

print(matrix[0][0])   # first element
print(matrix[1][2])   # last element


users = [
    [25, 50000, 2],
    [30, 70000, 5],
    [22, 30000, 1]
]

# Print all users
for user in users:
    print(user)

# Extract all ages
for user in users:
    print(user[0])