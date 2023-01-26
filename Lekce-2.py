#pekarna ma polozky a ceny v korunech
pekarna = {
    "houska": 10,
    "kolac" : 15,
    "chleba" : 40,
    "muffin" : 20,
    "loupak" : 20,
    "frgal" : 50
}
#klic je polozka, cena je hodnota, klic je jedinecna hodnota
produkty = ["houska", "kolac", "chleba"]
print(pekarna)
print(pekarna["kolac"]) # vypise hodnotu zadaneho klice
print("klic : frgal " + str(pekarna["kolac"]))


produkt = input("Zadej produkt: ")
if produkt in pekarna:
    print(f'{produkt} stoji {pekarna[produkt]} korun.')
else: #Pokud neni v pekarne = klic neni ve slovniku
    print(f'Bohuzel, produkt {produkt} neprodavame.')

pekarna["zavin"] = 150 #pridavame novy klic a hodnotu do dictionary
print(pekarna)

#pridani nekolika zaznamu do dictionary
nove_produkty = {"zavin": 150, "buchta":25, "donat":45}
pekarna.update(nove_produkty)
print(pekarna)

#uprava zaznamu v dictionary
pekarna["muffin"] = 22
print(pekarna)

#odebere cely zaznam 
cena_housky = pekarna.pop("houska")
print(pekarna)
print(cena_housky)