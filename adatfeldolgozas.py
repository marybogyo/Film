from Film import Film
filmlista = []
def beolvasas(): #def beolvas(fajlnev):
    #f=open(fajlnev,"r", encoding="utf-8")
    f = open("film.txt", "r", encoding= "utf-8")
    f.readline()
    sorok = f.readlines()
    f.close()
    feldolgoz(sorok)


def feldolgoz(sorok):
    i = 0
    while i < len(sorok):
        sorlista = sorok[i].strip().split(";")
        film = Film(sorlista)
        filmlista.append(film)
        i += 1

    print(filmlista[2].cim)

def filmekszama():

    return len(filmlista)

def legrovidebb_film_cim():
    min = filmlista[0].perc
    min_hely = 0
    i = 0
    while i < len(filmlista):
        if filmlista[i].perc <min:
            min = filmlista[i].perc
            min_hely = i
        i += 1
    return filmlista[min_hely].cim

def szaztizperc():
    i = 0
    szaztizpercdb = 0
    while i < len(filmlista):
        if (filmlista[i].perc >= 110):
            szaztizpercdb += 1
        i += 1
    return szaztizpercdb

'''    for elem in filmlista:
        if len(elem.perc) >= 110:
            szaztizpercdb += 1
    return szaztizpercdb'''

def filmajanlo():
    filmcime = []
    szineszneve = input("Kérem adjon megy egy színészt a kereséshez: ")
    i = 0
    while i < len(filmlista):
        if (filmlista[i].foszereplo == szineszneve):
            filmcime.append(filmlista[i].cim)

        i += 1
    if len(filmcime) <= 0:
        return "Nincs ilyen színésszel film"
    else:
        return filmcime

def fajl_beiras(eredmeny):
    fajl = open("Feladat3.txt", "w", encoding="utf-8")
    #fajl.write(str(szaztizperc()))
    fajl.write(str(eredmeny))
    fajl.close()