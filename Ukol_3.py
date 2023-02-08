import json
with open('body.json', encoding='utf-8') as soubor:
    body = json.load(soubor)
print(body)

for student, points in body.items(): 
    if points >= 60: 
        body[student] = 'Pass'
    
    else:
        body[student] = 'Fail'
        
print(body)

import json
with open('body3.json', mode='w', encoding='utf-8') as soubor:
    json.dump(body, soubor, ensure_ascii=False, indent=4)

#Mohl byste mi poradit proc body2.json file je uplne rozbity kvuli diakritice? Netusim co s tim mam udelat :(