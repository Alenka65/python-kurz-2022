sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}
product = input("Zadejte kod soucastky: ")
amount = int(input("Kolik kusu chcete koupit?: "))
total_amount = 0

if not product in sklad:
    print("Bohuzel, soucastka ", product, "neni skladem.")
elif amount > sklad[product]:
    print("Soucastka ", product, " je na sklade. Bohuzel mame jen ", sklad[product], "kusu." )
    item_sold = sklad.pop(product)
    print(sklad) #Vypsala jsem cely dictionary pro kontrolu, ale tenhle radek tady nemusi byt
else: 
    print("Soucastku ",product," mame na sklade. Objednavku lze uspokojit v plne vysi.")
    sklad[product] = sklad[product] - amount
    print(sklad) #Zase pro kontrolu jsem to vypsala :) 

## !!!! Odevzdavam dneska povinny ukol, zbytek nepovinnych udelam pozdeji a pridam do gitu