a = b = c = "Python 2023"

print(a == b)
print(b == c)

print(type(a), " - ", hex(id(a)))
print(type(b), " - ", hex(id(b)))
print(type(c), " - ", hex(id(c)))

c = "Java 11"

print(a == b)
print(b == c)

print(type(a), " - ", hex(id(a)))
print(type(b), " - ", hex(id(b)))
print(type(c), " - ", hex(id(c)))
