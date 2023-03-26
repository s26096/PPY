liczby = input("podaj liczby rozdzielone przecinkami: ")
liczby = liczby.split(",")

for ids, s in enumerate(liczby):
    liczby[ids] = int(liczby[ids])

maximum = liczby[0]
for i in liczby:
    if i > maximum:
        maximum = i

minimum = liczby[0]
for i in liczby:
    if i < minimum:
        minimum = i

print(maximum)
print(minimum)
