moja_lista = ["Warszawa", "Kraków", "Wrocław", "Łódź", "Poznań",
              "Gdańsk", "Szczecin", "Bydgoszcz", "Lublin", "Białystok", "nowe"]
for index in range(0, len(moja_lista)):
    print(moja_lista[index])
print(moja_lista.index("nowe", 0, 12))

liczby = list(range(1, 11, 3))
for element in liczby:
    print(element)


def func(n):
    print("Hello " + n)


func("Ello")


def prime(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break
    if is_prime:
        print(str(number) + " is proime")
    else:
        print(str(number) + " is not proimie")


prime(222)
