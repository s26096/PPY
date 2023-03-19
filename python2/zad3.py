qAndA = [["Najczęstszym sposobem spędzania wolnego czasu jest dla Ciebie:", "oglądanie telewizji/filmów/seriali", "czytanie książek/czasopism", "słuchanie muzyki"],
         ["W jakich okolicznościach czytasz książki najczęsciej?", "podczas podróży", "w czasie wolnym(po pracy, na urlopie", "podczas pracy/nauki(to ich element"],
         ["Jeżeli spędzasz czas wolny czytając ksiązki, jaki jest głowny powód taiego wyboru?", "chęc poszerzenia wiedzy", "czytanie mnie relaksuje/odpręża", "czytanie to moje hobby"],
         ["Po ksiązki w jakiej formie sięgasz najczęściej?", "papierowej(tradycyjnej)", "e-booki(ksiązki elektorniczne) na komputerze", "e-booki na tablecie/telefonie"]]
name = input("Podaj swoje imie i nazwisko: ")
answers = []

for idx, x in enumerate(qAndA):
    answers.append(int(input(f"{qAndA[idx][0]}\n1. {qAndA[idx][1]}\n2. {qAndA[idx][2]}\n3. {qAndA[idx][3]}\n")))

print(f"Podaj swoje imie i naziwisko: \nodpowiedź: {name}\n")
for i, ans in enumerate(answers):
    print(f"pytanie: {qAndA[i][0]}\nodpowiedź: {qAndA[i][ans]}\n")