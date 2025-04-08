def pituus():
    print("Valitse pituusyksikkö seuraavien joukosta syöttämällä suluissa annettu lyhenne")
    print("Tuuma (in tai \")")
    print("Jalka (ft tai ')")
    print("Jaardi (yd)")
    print("Maili (mi)")
    print()
    yksikko = input("Anna muutettava yksikkö: ")
    arvo = float(input("Anna muutettava arvo: "))
    if yksikko == "in" or yksikko == "\"":
        si_arvo = arvo * 2.54
        print(f"{arvo:.2f}\" on {si_arvo:.2f} cm")
    elif yksikko == "ft" or yksikko == "'":
        si_arvo = arvo * 30.48
        print(f"{arvo:.2f}' on {si_arvo:.2f} cm")
    elif yksikko == "yd":
        si_arvo = arvo * 0.9144
        print(f"{arvo:.2f} yd on {si_arvo:.2f} m")
    elif yksikko == "mi":
        si_arvo = arvo * 1.609344
        print(f"{arvo:.2f} mi on {si_arvo:.2f} km")
    else:
        print("Valitsemaasi yksikköä ei voida muuntaa")

def massa():
    print("Valitse painoyksikkö seuraavien joukosta syöttämällä suluissa annettu lyhenne")
    print("Unssi (oz)")
    print("Pauna (lb)")
    print()
    yksikko = input("Anna muutettava yksikkö: ")
    arvo = float(input("Anna muutettava arvo: "))
    if yksikko == "oz":
        si_arvo = arvo * 28.349523125
        print(f"{arvo:.2f} oz on {si_arvo:.2f} g")
    elif yksikko == "lb":
        si_arvo = arvo * 0.45359237
        print(f"{arvo:.2f} lb on {si_arvo:.2f} kg")
    else:
        print("Valitsemaasi yksikköä ei voida muuntaa")

def tilavuus():
    print("Valitse nestetilavuusyksikkö seuraavien joukosta syöttämällä suluissa annettu lyhenne")
    print("Kupillinen (cp)")
    print("Pintti (pt)")
    print("Varttigallona (qt)")
    print("Gallona (gal)")
    print()
    yksikko = input("Anna muutettava yksikkö: ")
    arvo = float(input("Anna muutettava arvo: "))
    if yksikko == "cp":
        si_arvo = arvo * 2.365882365
        print(f"{arvo:.2f} cp on {si_arvo:.2f} dl")
    elif yksikko == "pt":
        si_arvo = arvo * 4.73176473
        print(f"{arvo:.2f} pt on {si_arvo:.2f} dl")
    elif yksikko == "qt":
        si_arvo = arvo * 0.946352946
        print(f"{arvo:.2f} qt on {si_arvo:.2f} l")
    elif yksikko == "gal":
        si_arvo = arvo * 3.785411784
        print(f"{arvo:.2f} gal on {si_arvo:.2f} l")
    else:
        print("Valitsemaasi yksikköä ei voida muuntaa")

def lampotila():
    print("Lämpötilamuunnos Fahrenheit-asteista Celsius-asteiksi")
    fahrenheit = float(input("Anna lämpötila: "))
    celsius = (5 / 9) * (fahrenheit - 32)
    print(f"{fahrenheit:.2f} °F on {celsius:.2f} °C")

print("Tämä ohjelma muuntaa yhdysvaltalaisia yksiköitä SI-yksiköiksi")
print("Mahdolliset toiminnot:")
print("(P)ituus")
print("(M)assa")
print("(T)ilavuus")
print("(L)ämpotila")
print()
valinta = input("Tee valintasi: ").strip().lower()
if valinta == "p" or valinta == "pituus":
    pituus()
elif valinta == "m" or valinta == "massa":
    massa()
elif valinta == "t" or valinta == "tilavuus":
    tilavuus()
elif valinta == "l" or valinta == "lämpötila":
    lampotila()
else:
    print("Valitsemaasi toimintoa ei ole olemassa")
