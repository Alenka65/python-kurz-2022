# Tvůj program nejprve ověří pomocí první funkce správnost telefonního čísla. Pokud není platné, vypíše chybu, v opačném případě se zeptá na text zprávy a pomocí druhé funkce určí její cenu, kterou vypíše uživateli.

# 1 Zeptá se uživatele na číslo, kam chce zprávu zaslat a ověří, že číslo má správný formát.

tel_cislo = input("Zadej telefonni cislo: ")
def overeni_tel_cisla (tel_cislo):
    """ První funkce ověří telefonní číslo. Uvažuj, že telefonní číslo může být devítimístné nebo třináctimístné (pokud je na začátku předvolba "+420"). Funkce ověří, jestli je číslo platné. Pokud je platné, vrátí hodnotu True, jinak vrátí hodnotu False."""
    kontrola = kontrola = tel_cislo[:4]
    if len(tel_cislo) == 13 and kontrola == '+420': 
        return True
    elif len(tel_cislo) == 9:
        return True
    else:
        return False

overeni_tel_cisla(tel_cislo)

# 2 Zeptá se uživatele na zprávu, kterou chce zaslat. Následně vypíše, kolik zpráva bude stát.
zprava = input("Zadej zpravu: ")
def vypocet_ceny_zpravy (zprava):
    """ Druhá funkce spočte cenu zprávy. Uživatel platí 3 Kč za každých započatých 180 znaků."""
    cena = 3 * (len(zprava)/180)
    print(f"Cena zpravy je {cena} kc")

vypocet_ceny_zpravy(zprava)

#Komentar k 2ce, ja si nejsem jista jestli je to spravne matematicky a nevim prijit na to, jak to spravne napsat :(