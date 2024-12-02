import random

kiekot = [['🍒', '🍓','🍐', '🍋', '🍉'], ['🍒', '🍓','🍐', '🍋', '🍉'], ['🍒', '🍓','🍐', '🍋', '🍉']]
tulos = []
saldo = 10

while True:
    saldo -= 1
    tulos.clear()


    for alilista in kiekot:
        tulos.append(random.choice(alilista))
    
    print(tulos)
    
    
    if tulos[0] == tulos[1] == tulos[2]:
        saldo += 5
        print("Voitit!")
    
    
    print(f"Saldosi on {saldo} rahaa.")
    vastaus = input("Haluatko jatkaa (k/e) > ")
    
    
    if vastaus.lower() == 'e' or saldo == 0:
        print(f"Sinulle jäi {saldo} rahaa")
        break


