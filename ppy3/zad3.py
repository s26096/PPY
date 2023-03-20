ilosc_rund = input("Podaj ilosc rund: ")
results = []

wybor = input("wybierz tryb: 1.komputer  2.hot seats: ")
if int(wybor) == 1:
    name1 = input("Podaj swoją nazwe: ")
    name2 = "komputer"

    for i in range(0, int(ilosc_rund)):


elif int(wybor) == 2:
    name1 = input("Podaj nazwe pierwszego gracza: ")
    name2 = input("Podaj nazwę drugiego gracza: ")

else:
    print("Nieprawidłowy tryb gry")
