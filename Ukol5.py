# Zadani: Mějme zadaný následující seznam naměřených teplot. Seznam obsahuje teploty naměřené pro každý den v týdnu ve čtyřech časech - ráno, v poledne, večer a v noci.

teploty = [
    [2.1, 5.2, 6.1, -0.1],
    [2.2, 4.8, 5.6, -1.0],
    [3.3, 6.5, 5.9, 1.2],
    [2.9, 5.6, 6.0, 0.0],
    [2.0, 4.6, 5.5, -1.2],
    [1.0, 3.2, 2.1, -2.0],
    [0.4, 2.7, 1.3, -2.8]
]

# 1) Vytvoř seznam průměrných teplot pro každý den.
prumerne_teploty = []

for teplota in teploty:
    avg = round(sum(teplota)/len(teplota)) #Pridala jsem round(), aby to pekne vypadalo
    prumerne_teploty.append(avg)
print(prumerne_teploty)

# 1) List comprehension version:
prumerne_teploty = [round(sum(teplota)/len(teplota)) for teplota in teploty]
print(prumerne_teploty)

# 2) Vytvoř seznam ranních teplot.
ranni_teploty = []

for teplota in teploty:
   ranni_teplota = teplota[0]
   ranni_teploty.append(ranni_teplota)

print(ranni_teploty)

# 2) List comprehension:

ranni_teploty = [teplota[0] for teplota in teploty]
print(ranni_teploty)

# 3) Vytvoř seznam nočních teplot.
nocni_teploty = []

for teplota in teploty:
    nocni_teplota = teplota[-1]
    nocni_teploty.append(nocni_teplota)

print(nocni_teploty)

# 3) List comprehension: 

nocni_teploty = [ teplota[-1] for teplota in teploty]
print(nocni_teploty)

# 4) Vytvoř seznam dvouprvkových seznamů obsahujících pouze polední a noční teplotu.

poledni_teploty = []

for teplota in teploty:
    poledni_teplota = teplota[1]
    poledni_teploty.append(poledni_teplota)

seznam_polednich_nocnich_teplot = []
seznam_polednich_nocnich_teplot.append(poledni_teploty)
seznam_polednich_nocnich_teplot.append(nocni_teploty)

print(seznam_polednich_nocnich_teplot)

# 4) List comprehension: 

poledni_teploty = [teplota[1] for teplota in teploty]

seznam_polednich_nocnich_teplot = [poledni_teploty, nocni_teploty]
print(seznam_polednich_nocnich_teplot)