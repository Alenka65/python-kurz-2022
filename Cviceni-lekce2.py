vysvedceni = {
    "matematika": 1,
    "cestina" : 2,
    "dejepis" : 1,
}
print(vysvedceni)

sales = {
    "Zkus mě chytit": 4165,
    "Vrah zavolá v deset": 5681,
    "Zločinný steh": 2565,
}
#pridani nove knizky
new_sales = {
    "Noc, která mě zabila" : 0
}

sales.update(new_sales)
print(sales)

#uprava Vrah zavolá v deset
sales["Vrah zavolá v deset"] = 5781
print(sales)


#Tombola
tombola = {
    7: "Láhev kvalitního vína Château Headache",
    15: "Pytel brambor z místního družstva",
    23: "Čokoládový dort",
    47: "Kniha o historii města",
    55: "Šiška salámu",
    67: "Vyhlídkový let balónem",
    79: "Moderní televizor",
    91: "Roční předplatné městského zpravodaje",
    93: "Společenská hra Sázky a dostihy",
}
cislo_listku = int(input("Zadej cislo : "))
if cislo_listku in tombola:
    print ("Vyhral jste: " + tombola[cislo_listku])
    vyhra = tombola.pop(cislo_listku)
    print (vyhra)
    print(tombola)
else: 
    print("Bohuzel nevyhravas nic")
