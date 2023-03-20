liczby = input("podaj liczby rozdzielone przecinkami: ")
liczby = liczby.split(",")

for ids, s in enumerate(liczby):
    liczby[ids] = int(liczby[ids])

max = liczby[0]
for i in liczby:
    if i > max:
        max = i

min = liczby[0]
for i in liczby:
    if i < min:
        min = i

print(max)
print(min)