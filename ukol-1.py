#Napiš program, který bude obsahovat jednu proměnnou jmeno. Tato proměnná bude obsahovat libovolné křestní jméno (třeba tvoje). Tvůj program vytvoří e-mailovou adresu na základě této proměnné, s doménou czechitas.cz a tuto e-mailovou adresu vypíše. Tedy pokud bude hodnota proměnné jmeno například Jindřiška, pak program vypíše Jindřiška@czechitas.cz

# prvni reseni
jmeno = "Alena_Rudykh"
print(jmeno + "@czechitas.cz")

#druhe reseni
jmeno = "Alena"
prijmeni = "Rudykh"
domena = "@czechitas.cz"
print(jmeno+prijmeni+domena)


#Napiš program, který bude obsahovat proměnnou jmeno_a_prijmeni. Obsah proměnné načti od uživatele pomocí funkce input. Tvůj program postupně vypíše několik způsobů formátování jména:

jmeno_a_prijmeni = input("Zadej svoje jmeno a prijmeni: ")
print(jmeno_a_prijmeni)

#všechna písmena velká (vypíše např. JANA MALÁ)
print(jmeno_a_prijmeni.upper())

#všechna písmena malá (vypíše např. jana malá)
print(jmeno_a_prijmeni.lower())

#standardní varianta - první písmeno velké, další malá (vypíše např. Jana Malá) -> pokud zadam svoje jmeno "Alena Rudykh" :D
print(jmeno_a_prijmeni[0].upper()+jmeno_a_prijmeni[1:5].lower()+" "+jmeno_a_prijmeni[6].upper()+jmeno_a_prijmeni[7:].lower())
#fix
print(jmeno_a_prijmeni.title())
#anebo takhle:
name = jmeno_a_prijmeni.split()
print(name)
print(name[0][0].upper()+ name[0][1:] + " " + name[1][0].upper() + name[1][1:])

#iniciály (vypíše např. J. M.).
print(jmeno_a_prijmeni[0].upper() +"." +" "+ jmeno_a_prijmeni[6].upper()+".")
#fix
print(name[0][0].upper()+"." + " " + name[1][0].upper() + ".")
