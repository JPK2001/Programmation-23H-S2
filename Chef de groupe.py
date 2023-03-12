import random
chefs=[]
etudiants=[]
while len(chefs)<5:
    v=random.choice(etudiants)
    if v not in chefs:
        chefs.append(v)
print(chefs)