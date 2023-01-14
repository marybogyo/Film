import adatfeldolgozas

adatfeldolgozas.beolvasas()
#adatfeldolgozas.beolvasas("film.txt")
print("1. feladat:")
print(f"\t Filmek száma : {adatfeldolgozas.filmekszama()}")

print("2. feladat:")
print(f"\t A legrövidebb film címe : {adatfeldolgozas.legrovidebb_film_cim()}")

print("3. feladat:")
print(f"\t 110 percnél hosszabb filmek száma : {adatfeldolgozas.szaztizperc()}")

print("4. feladat:")
eredmeny = adatfeldolgozas.filmajanlo()
print(f"\t Filmajánló : {eredmeny}")

print("5. feladat:")
adatfeldolgozas.fajl_beiras(eredmeny)
