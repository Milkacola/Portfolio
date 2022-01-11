import random

def pakli():
    kartyak = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    rand_kartya = random.choice(kartyak)
    return rand_kartya

def pontszamolas(kartyak):
    if sum(kartyak) == 21 and len(kartyak) == 2:
        return 0
    if 11 in kartyak and sum(kartyak) > 21:
        kartyak.remove(11)
        kartyak.append(1)
    return sum(kartyak)

def pont_osszehasonlitas(gepkartya, jatekos_kartya):
    if jatekos_osszes == geposszes :
        return "Döntetlen!"
    elif jatekos_osszes > 21:
        return "A gép nyert!"
    elif geposszes > 21:
        return "Te nyertél!"
    elif jatekos_osszes > geposszes :
        return "Te nyertél!"
    else:
        return "A gép nyert!"


jatekos_kartya = []
gepkartya = []
jatek_vege = False

for i in range(2):
    jatekos_kartya.append(pakli())
    gepkartya.append(pakli())


jatekos_osszes = pontszamolas(jatekos_kartya)
geposszes = pontszamolas(gepkartya)

while not jatek_vege:
    jatekos_osszes = pontszamolas(jatekos_kartya)
    geposszes = pontszamolas(gepkartya)
    print(f"A te kártyáid: {jatekos_kartya} pontod: {jatekos_osszes}")
    print(f"A gép első kártyája: {gepkartya[0]} ")

    if jatekos_osszes == 0 or geposszes == 0 or jatekos_osszes > 21:
        jatek_vege = True
    else:
        hit = input("Írj H hogy húzz vagy M hogy megállj: ").upper()
        if hit == "H":
            jatekos_kartya.append(pakli())
        else:
            jatek_vege = True

while geposszes != 0 and geposszes < 17:
    gepkartya.append(pakli())
    geposszes = pontszamolas(gepkartya)
    print(f"A gép kártyái: {gepkartya}")
    print(f"A gép pontja: {geposszes}")

print(pont_osszehasonlitas(geposszes, jatekos_osszes))