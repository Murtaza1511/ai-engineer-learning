# Vector Addition

a = [1,2,3]
b = [4,5,6]

result = []

for i in range(len(a)):
    result.append(a[i] + b[i])

print(result)

# Vector Subtraction
c = [7,8,9]
d = [1,2,3]

result2 = []

for i in range(len(c)):
    result2.append(c[i] - d[i])

print(result2) 

# Dot Product

e = [1,2,3]
f = [4,5,6] 
dot_product = 0

for i in range(len(e)):
    dot_product += e[i] * f[i]

print(dot_product)