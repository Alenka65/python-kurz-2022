sales = {
    "Zkus mě chytit": 4165,
    "Vrah zavolá v deset": 5681,
    "Zločinný steh": 2565,
}

#Pri prochazeni pres dictionary prochazime pres jeho klice (nazvy knizek u nas)
for nazev in sales: 
    print(nazev)
    #print("Knihy s nazvem "+ nazev + "se prodalo " + sales[nazev] + "ks.")
    print(f'Knihy s nazvem {nazev} se prodalo {sales[nazev]} ks.')

#Jake jsou klice slovniku? 
print(sales.keys())

#Jake jsou hodnoty slovniku?
print(sales.values())

#Kolik se prumerne prodalo vytisku na knihu?
print(sum(sales.values())/ len(sales))

print(sales.items())

for nazev, prodano in sales.items(): #Dvojice klic, hodnota
    print(f'Knihy s nazvem {nazev} se prodalo {prodano} ks.')