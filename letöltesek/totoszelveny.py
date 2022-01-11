import random #könyvtár importálása lásd lejebb

print(
    """
    1. feladat: Totószelvény
    A program generáljon le egy véletlenszerű totószelvényt és legyen ez az aktuális heti nyertes szelvény! 
    Ezután a program generáljon le N(>0) db véletlenszerű totószelvényt és összesítve adjon konzolos értékelést arról, 
    hogy melyik szelvény(ek) volt(ak) nyertes(ek) az ismert játékszabály alapján! 
    Többféleképpen is specifikálható a nyertes állapot: legalább 10 egyezés, pontosan 10, 11, … egyezés.
    """
)

#az aktuális heti nyertes szelvény legenerálása
#a szüksége számok generálásához minden helyen a random könyárat használjuk (https://docs.python.org/3/library/random.html)
nyertes_szelveny = []

for i in range(0,14): #ezzel a ciklussal létrehozzuk a nyertes szelvényt egy lista formájában
    n = random.randint(1,3)
    nyertes_szelveny.append(n)
print(f"A nyertes totószelvény számai: {nyertes_szelveny}")

osszesSzelveny = [] #ez a lista fogja tárolni a szelvényeket

for j in range(random.randint(10000,15000)): #legenerálunk random számú szelvényt(https://docs.python.org/3/library/random.html#random.randint)
    szelveny = []

    for i in range(0,14):#egy darab szelvény létrehozása szintén listaként
        n = random.randint(1,3)
        szelveny.append(n)
    print(f"A(z) {j+1}. szelvény számai: {szelveny}")
    osszesSzelveny.append(szelveny) #hozzácsatoljuk az aktuálisan generált szelvényt az összes szelvényt tartalmazó listához(osszesSzelveny)

#a 10 vagy annál több eggyezést tartalmazó szelvényeket a szelvény sorszáma alapján listákba mentjük 
#ezért létrehozzuk az alábbi listákat
tizesek = []
tizenegy = []
tizenketto = []
tizenharom = []
tizennegy = []

szelvenyszamlalo = 0 #ez a változó tárolja az aktuális szelvény sorszámát
for i in osszesSzelveny: #ebben a ciklusban összehasonlítjuk a létrehozott szelvényeket a nyertes szelvénnyel 
    talalat = 0
    szelvenyszamlalo += 1
    for j in range(0,14):
        if i[j] == nyertes_szelveny[j]:
            talalat += 1
        
    if talalat == 10: #amennyiben egy szelvény legalább 10 találatos sorszám alapján hozzácsatoljuk a megfelelő listához
        tizesek.append(szelvenyszamlalo)
    elif talalat == 11:
        tizenegy.append(szelvenyszamlalo)
    elif talalat == 12:
        tizenketto.append(szelvenyszamlalo)
    elif talalat == 13:
        tizenharom.append(szelvenyszamlalo)
    elif talalat == 14:
        tizennegy.append(szelvenyszamlalo)
    else:
        pass 

#meghatározzuk az összes találat számát a találatokat tartalmazó listák hossza alapján (https://docs.python.org/3/library/functions.html#len)
osszestalalat = len(tizesek) + len(tizenegy) + len(tizenketto) + len(tizenharom) + len(tizennegy) 
#kiírjuk a találatokat egyenként
print(f"Összes találat száma: {osszestalalat}")
print(f"Tizes találatok száma: {len(tizesek)}")
print(f"Tizes szelvények: ")
for i in tizesek:
    print(f"{i}. ")

print(f"Tizenegyes találatok száma: {len(tizenegy)}")
print(f"Tizenegyes szelvények: ")
for i in tizenegy:
    print(f"{i}. ")

print(f"Tizenkettes találatok száma: {len(tizenketto)}")
print(f"Tizenkettes szelvények: ")
for i in tizenketto:
    print(f"{i}. ")

print(f"Tizenhármas találatok száma: {len(tizenharom)}")
print(f"Tizenhármas szelvények: ")
for i in tizenharom:
    print(f"{i}. ")

print(f"Tizennégyes találatok száma: {len(tizennegy)}")
print(f"Tizennégyes szelvények: ")
for i in tizennegy:
    print(f"{i}. ")

#For more informaion please visit https://www.youtube.com/watch?v=iik25wqIuFo 