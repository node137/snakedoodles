import math

def laske_nelion_ala(sivun_pituus):
    nelion_ala = sivun_pituus ** 2
    return nelion_ala

def laske_sektorin_ala(sade, sisakulma):
    sektorin_ala = sisakulma / 360 * math.pi * sade ** 2
    return sektorin_ala

def laske_sivun_pituus(hypotenuusa):
    kateetti = hypotenuusa /  math.sqrt(2)
    return kateetti

def laske_kuvion_ala(arvo):
    pikkunelion_ala = laske_nelion_ala(arvo)
    pikkukolmion_kateetti = laske_sivun_pituus(arvo)
    pikkukolmion_ala = pikkukolmion_kateetti * pikkukolmion_kateetti / 2
    pikkusektorin_ala = laske_sektorin_ala(pikkukolmion_kateetti, ((180-90)/2))
    isonelion_ala = laske_nelion_ala(pikkukolmion_kateetti*2)
    isosektorin_ala = laske_sektorin_ala(pikkukolmion_kateetti*2,360-90)   
    
    kuvion_pinta_ala = pikkunelion_ala + pikkukolmion_ala + pikkusektorin_ala
    kuvion_pinta_ala = kuvion_pinta_ala + isonelion_ala + isosektorin_ala
    
    return kuvion_pinta_ala

# pääohjelma joka kysyy x:n arvon
x = float(input("Anna x: "))
# kutsuu laskufunktiota ja tulostaa alan
# pyöristettynä
print("Kuvion ala: ", round(laske_kuvion_ala(x),4))
