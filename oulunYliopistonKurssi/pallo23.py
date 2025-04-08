import math

def laske_ala(sade):
    return 4 * math.pi * sade ** 2
    
def laske_tilavuus(sade):
    return 4 / 3 * math.pi * sade ** 3

def laske_sade(piiri):
    return piiri / (math.pi * 2)

def laske_pallon_ominaisuudet(piiri):
    sade = laske_sade(piiri)
    ala = laske_ala(sade)
    tilavuus = laske_tilavuus(sade)
    return ala, tilavuus
    
mitattu_piiri = float(input("Anna pallon ympärysmitta: "))
laskettu_ala, laskettu_tilavuus = laske_pallon_ominaisuudet(mitattu_piiri)
print("Tilavuus:", round(laskettu_tilavuus, 4))
print("Pinta-ala:", round(laskettu_ala, 4))