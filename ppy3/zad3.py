import random
import getpass

ilosc_rund = input("Podaj ilosc rund: ")
results = []

opcja = input("wybierz tryb: 1.komputer  2.hot seats: ")
if int(opcja) == 1:
    name1 = input("Podaj swoją nazwe: ")
    name2 = "Komputer"

    for i in range(0, int(ilosc_rund)):
        while True:
            wybor = int(input("Wybierz: 1.papier   2.kamien   3.nozyce\n"))
            komp = random.randint(1, 3)

            if wybor == komp:
                print("Remis!")
            elif wybor == 1:
                if komp == 2:
                    print("papier bije kamien - wygrywasz!")
                    results.append(name1)
                    break
                else:
                    print("nozyce pokonuja papier - przegrywasz")
                    results.append(name2)
                    break
            elif wybor == 2:
                if komp == 1:
                    print("papier bije kamien - przegrywasz")
                    results.append(name2)
                    break
                else:
                    print("kamien pokonuje nozyce - wygrywasz!")
                    results.append(name1)
                    break
            elif wybor == 3:
                if komp == 1:
                    print("nozyce pokonuja papier - wygrywasz!")
                    results.append(name1)
                    break
                else:
                    print("kamien pokonuje nozyce - przegrywasz")
                    results.append(name2)
                    break
            else:
                print("Nieprawidłowy wybor")

elif int(opcja) == 2:
    name1 = input("Podaj nazwe pierwszego gracza: ")
    name2 = input("Podaj nazwę drugiego gracza: ")

    for i in range(0, int(ilosc_rund)):
        while True:
            w1 = int(getpass.getpass(f"{name1}: 1.papier   2.kamien   3.nozyce\n"))
            w2 = int(getpass.getpass(f"{name2}: 1.papier   2.kamien   3.nozyce\n"))
            if w1 == w2:
                print("Remis!")
            elif w1 == 1:
                if w2 == 2:
                    print(f"papier bije kamien - wygrywa {name1}!")
                    results.append(name1)
                    break
                else:
                    print(f"nozyce pokonuja papier - wygrwa {name2}")
                    results.append(name2)
                    break
            elif w1 == 2:
                if w2 == 1:
                    print(f"papier bije kamien - wygrywa {name2}")
                    results.append(name2)
                    break
                else:
                    print(f"kamien pokonuje nozyce - wygrywa {name1}")
                    results.append(name1)
                    break
            elif w1 == 3:
                if w2 == 1:
                    print(f"nozyce pokonuja papier - wygrywa {name1}")
                    results.append(name1)
                    break
                else:
                    print(f"kamien pokonuje nozyce - wygrywa {name2}")
                    results.append(name2)
                    break
            else:
                print("Nieprawidłowy wybor")

else:
    print("Nieprawidłowy tryb gry")
i = 0
counter = 0
print("\nWyniki:\n")
for r in results:
    i += 1
    print(f"W {i} rundzie wygral: {r}")
    if r == name1:
        counter += 1

if counter > int(ilosc_rund)-counter:
    print(f"Grę wygrał {name1}")
elif counter < int(ilosc_rund)-counter:
    print(f"Grę wygrał {name2}")
else:
    print("Remis!")
