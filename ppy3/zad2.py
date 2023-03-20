import random

cities = "Warszawa,Kraków,Wrocław,Łódź,Poznań,Gdańsk,Szczecin,Bydgoszcz,Lublin,Białystok"
cities_list = cities.split(",")

while len(cities_list) > 0:
    r = random.randint(0,len(cities_list)-1)
    print(cities_list[r])
    del cities_list[r]