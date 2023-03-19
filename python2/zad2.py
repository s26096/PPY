num1 = float(input("Podaj pierwsza liczbe: "))
char = input("Podaj znak: ")
num2 = float(input("Podaj drugą liczbe: "))
result = 0

if char == "+":
    result = num1 + num2
elif char == "-":
    result = num1 - num2
elif char == "/":
    result = num1 / num2
elif char == "*":
    result = num1 * num2

print(result)