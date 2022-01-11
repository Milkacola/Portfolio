print(
    """
    3. Brit érmék
    Az Egyesült Királyságban 8-féle érme van forgalomban. Ezek a következők (pound (£) és penny (p)): 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), és £2 (200p).
    £2-ot például így lehet kifizetni: 1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p. Tudjuk, hogy 73682-féleképpen lehet kifizetni £2-ot úgy, hogy bármilyen érméből bármennyit felhasználhatunk.
    A program írja ki a lehetséges kifizetéseket külön sorokban a konzolra úgy, hogy a ciklusok lépésszáma 3000000 alatt legyen!
    """)

ketfont = 200 #a kétfontos kifizetést egy külön változóban adjuk meg
ermek = [1,2,5,10,20,50,100,200]

lehetlista = [[erme] for erme in ermek] #ez a sor alapvetően egy listát hoz létre a listában, amin belül az érmékkel dolgozunk, https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
lehetosegek = [] #az egyes lehetőségeket tároló lista
osszes = [] #az összes különböző lehetőséget tároló lista
while lehetlista:
    for aktualislehetoseg in lehetlista:
        s = sum(aktualislehetoseg) #összeadja az aktualislehetoseg lista elemeit
        for erme in ermek:
            if erme >= aktualislehetoseg[-1]:
                if s + erme < ketfont: #a program itt nézi meg, hogy az éppen vizsgált lehetőség lista számainak összege elére-e a 200-at
                    lehetosegek.append(aktualislehetoseg + [erme]) #ha nem akkor hozzáad még egy elemet és újra leellenőrzi
                elif s + erme == ketfont: #ha pedig igen akkor azt a listát hozzáadja az összes lehetőség listához
                    osszes.append(aktualislehetoseg + [erme])
    lehetlista = lehetosegek
    lehetosegek = []


osszes.insert(0,[200]) #az összes lehetőség listájához hozzáadjuk az egy darab kétfontossal való kifizetést
for i in osszes:
    print(i) #itt írjuk ki egyesével a lehetőségeket

print(f"Összes lehetőség száma: {len(osszes)}")

#a program lefutása a gomb megnyomásától a végéig kb. 30mp-ig tart