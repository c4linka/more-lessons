"""
lesson:

myCats = [
    ["Kota", "4,5kg", "female"],
    ["Rysia", "5kg", "female"],
    ["Knypuś", "3,7kg", "female"]
    ]
print(myCats)

myCats[1][1] = "5,1kg" #zmiana danych wg indeksu

print(myCatsmyCats = [
    ["Kota", "4,5kg", "female"],
    ["Rysia", "5kg", "female"],
    ["Knypuś", "3,7kg", "female"]
    ]

myCats.append[0][4] = ["color" "tortoise"]
print(myCats)

for name, weight, sex in myCats:
    print("Cat's name:", name)
    print("Cat's weight:", weight)
    print("Cat's sex:", sex)
    print("\n")

myCats.append(("New Cat", "2kg", "male"))

print(myCats)

for name, weight, sex in myCats:
    print("Cat's name:", name)
    print("Cat's weight:", weight)
    print("Cat's sex:", sex)
    print("\n")
)

"""
from pprint import pprint

myCats = [
    ["Kota", "4,5kg", "female"],
    ["Rysia", "5kg", "female"],
    ["Knypuś", "3,7kg", "female"]
    ]

print(myCats[0])



print(myCats)


for cat in myCats:
    cat.append("tortoiseshell")
pprint(myCats)

print()

for name, weight, sex, color in myCats:
    print("Cat's name:", name)
    print("Cat's weight:", weight)
    print("Cat's sex:", sex)
    print("Cat's color:", color)
    print("\n")
 

myCats.append(["New Cat", "2kg", "male"])

pprint(myCats)
print()

myCats[3].append("black")

pprint(myCats)




















