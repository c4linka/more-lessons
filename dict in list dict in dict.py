"""
#dictionary and list in lists lesson

# TO JEST SAM ZBIÓR CZY SŁOWNIK? JAK TO ODRÓŻNIĆ? raczej słownik bo jest "cos" i dwukropek

ratings1 = {     
    "Ala": (1, 2, 3),
    "Ewa": (4, 5, 6)
    }
print(ratings1["Ewa"])

#print(4, 4 **4)  - wyjasnienie, że zapis 4 zmienia ;)

for key, val in ratings1.items(): # TO JEST TO SAMO CO  26ta XXXXX
    print(key + "'s ratings:", val)


for key in ratings1:    #wypisze same imiona
    print(key)
    

for key in ratings1:    #wypisze same oceny
    print(ratings1[key])
   

for key in ratings1:     #wypisze imiona i oceny TO TO SAMO CO  14ta XXXXX
    print(key + "'s ratings:", ratings1[key]) #wybieranie warotosci klucza key poprzez stawianie nawiasu kwadratowego za nazwa slwonika 
#--------------------------------------------------------------------------
"""
# TO JEST SŁOWNIK W LIŚCIE
"""
ratings2 = [
    {"name": "Ela", "ratings": (1, 2, 3), "behaviour": 6},
    {"name": "Andrzej", "ratings": (4, 5, 6), "behaviour": 1}
    ]

 


people2 = [
    {"id": "personA", "name": "John", "age": 27, "sex": "male"},
    {"id": "personB", "name": "Mat", "age": 37, "sex": "male"},
    {"id": "personC", "name": "Jane", "age": 47, "sex": "female"}
    ]

for person in people2:
    for key in person:
        print(key, person[key])   #wypisze kolejno kazda person A B C i key + val - cięgiem

for person in people2:
    for key in person:
        print(key, person[key])
        print()                  #wypisze kazdy key z enterem, bo petla odnosi sie do key w kazdej osobie

for person in people2:    #jak sie chce wszystkie persony wypisac to pętlą
    for key in person:
        print(key, person[key])
    print()    
        
        
print("name:", people2[1]["name"]) #wypisze -> name: Mat

print(people2[1]) #wypisze cala linijke pesonB
"""
#-------------------------------------------------------------------------
# TO JEST SŁOWNIK W SŁOWNIKU #info["behaviour"] ->wyrazenie krote zwraca wartosc danego klucza

journal3 = {
    "Mo": {"ratings": (4, 3, 4), "behaviour": 5},
    "Wo": {"ratings": (1, 2, 1), "behaviour": 2},
    "Jo": {"ratings": (1, 1, 1), "behaviour": 6},
    }


#chce zeby wynikiem bylo:    
#Name: Mo Ratings: 4 3 2 Behaviour: 5        
#Name: Wo Ratings: 1 2 3 Behaviour: 2
#Name: Wo Ratings: 1 2 3 Behaviour: 2:

for name in journal3:   #name to jest samo "Mo" i "Wo" i "Jo" - tyle razy wykona iteracje ile wpisów w słowniku (imion i jednoczesnie tyle samo musi byc słownikow nazwanych imionami)
    info = journal3[name]   #info to jest cale to {"ratings": (4, 3, 4), "behaviour": 5}
    degr = info["ratings"]       #degr to oceny w (nawiasach) zapisane jako info["behaviour"]
    beh  = info["behaviour"]  #dobranie się do wartości "behaviour" ze zmiennej info
    print("Name:", name + ",", "Ratings:", str(degr) + ",", "Behaviour:", beh)

#wypisac tylko jedna osobe
print()
name = "Wo"
info = journal3[name]   #info to jest cale to {"ratings": (4, 3, 4), "behaviour": 5}
degr = info["ratings"]       #degr to oceny w (nawiasach) zapisane jako info["behaviour"]
beh  = info["behaviour"]  #dobranie się do wartości "behaviour" ze zmiennej info
print("Name:", name + ",", "Ratings:", str(degr) + ",", "Behaviour:", beh)

print("Name:", "Wo, Ratings:", str(journal3["Wo"]["ratings"]) + ",", "Behaviour:", journal3["Wo"]["behaviour"])
print()
from pprint import pprint
journal4 = list(journal3.items())
pprint(journal4[1])

people1= {
    "person1": {"name": "Anna", "age": 20, "sex": "female"},
    "person2": {"name": "Adam", "age": 30, "sex": "male"},
    "person3": {"name": "Ola", "age": 40, "sex": "female"}
    }
#--------------------------------------------------------------------------


