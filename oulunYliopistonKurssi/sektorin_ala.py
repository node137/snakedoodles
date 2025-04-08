import math

def laske_sektorin_ala(sade, sisakulma):
    # sektoritehtävän funktion koodi
    sektorin_ala = sisakulma / 360 * math.pi * sade ** 2
    return sektorin_ala

alku_sade = float(input("Anna ympyrän säde: "))
alku_sisakulma = float(input("Anna sektorin sisäkulma asteina: "))
print("Sektorin pinta-ala: ", round(laske_sektorin_ala(alku_sade, alku_sisakulma),4))
