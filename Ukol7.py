class Auto:
    """ Tvorba tridy Auto"""

    def __init__(self, registracni_znacka, znacka_a_typ_vozidla, pocet_najetych_km):
        self.registracni_znacka = registracni_znacka
        self.znacka_a_typ_vozidla = znacka_a_typ_vozidla
        self.pocet_najetych_km = pocet_najetych_km
        self.dostupne = True
    
    def pujc_auto(self):
        if self.dostupne == True:
            self.dostupne = False
            print("Potvrzuji zapůjčení vozidla")
        else: 
            print("Vozidlo není k dispozici")

    def get_info(self):
        print(f"Registrační značka vozidla: {self.registracni_znacka}")
        print(f"Značka a typ vozidla: {self.znacka_a_typ_vozidla}")

#Tady jsem vytvorila promenne skoda a peugeot a pridala jsem je informace dle tabulky z ukolu
peugeot = Auto("4A2 3020","Peugeot 403 Cabrio", 47534)
skoda = Auto("1P3 4747", "Škoda Octavia", 41253)

#Vytvorila jsem promennou kterou pouziju jako input od zakaznika
zapujcene_auto = input("Vyber znacku auta (skoda/peugeot): ")

#Tohle jsem musela napsat aby to cele fungovalo, jinak pro input string mi neslo pridat metody
if zapujcene_auto == "skoda":
    zapujcene_auto = skoda
elif zapujcene_auto == "peugeot":
    zapujcene_auto = peugeot

#Zkousela jsem 2x pujcit stejne auto a nejde to :) Vypada to, ze kod funguje
zapujcene_auto.get_info()
zapujcene_auto.pujc_auto()



