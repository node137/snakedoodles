import random
import sys
import time
import turtle as t

LEVEYS = 800
KORKEUS = 600
NAPPI_LEVEYS = 200
NAPPI_KORKEUS = 60

VASEN = 0
OIKEA = 1
YLA = 2
ALA = 3

ikkuna = []
tila = {
    "piirto": False,
    "kaynnissa": False
}


def luo_ikkuna(otsikko):
    """
    Luo "ikkunan" johon käyttöliittymän kehykset ja elementit voidaan kerätä.
    Tässä approksimaatiossa ikkuna on vain lista, johon elementit
    lisätään. Tämä funktio ainoastaan tyhjää olemassaolevan ikkunalistan.
    """
    
    ikkuna.clear()
    return ikkuna
    
def luo_kehys(isanta, puoli=VASEN):
    """
    Luo kehyksen. Tämä funktio hieman huijaa, ja lisää kehyksen suoraan
    ikkunaan riippumatta siitä mitä parametrien arvot ovat. Kirjasto ei siis
    tue sisäkkäisiä kehyksiä, eikä alekkaisia kehyksiä. 
    """

    kehys = []
    ikkuna.append(kehys)
    return kehys

def luo_nappi(kehys, teksti, toiminto):
    """
    Luo napin, eli lisää kehykseen nappia kuvaavan sanakirjan. Napin sijainti
    lasketaan kehyksen indeksistä ikkunan sisällä sekä kehyksessä jo olevien
    nappien lukumäärästä siten, että napin leveydeksi tulee NAPPI_LEVEYS ja korkeudeksi
    NAPPI_KORKEUS yksikköä.
    """
    
    vasen = ikkuna.index(kehys) * NAPPI_LEVEYS
    oikea = vasen + NAPPI_LEVEYS
    yla = len(kehys) * NAPPI_KORKEUS
    ala = yla + NAPPI_KORKEUS
    kehys.append({
        "vasen": vasen,
        "oikea": oikea,
        "yla": yla,
        "ala": ala,
        "teksti": teksti,
        "toiminto": toiminto
    })
    
def lue_klikkaus():
    """
    Funktio joka tuottaa uuden "klikkauksen". Toistaiseksi generoi satunnaisen
    pisteen joka on "ikkunan" rajojen sisällä.
    """
    
    x = random.randint(0, LEVEYS - 1)
    y = random.randint(0, KORKEUS - 1)
    return x, y
    
def tunnista_nappi(x, y, ikkuna):
    """
    Etsii mihin nappiin klikkaus osui ikkunan sisällä, jos mihinkään. 
    Mikäli klikkaus osui nappin rajojen sisälle, kutsuu nappiin kiinnitettyä
    toiminto-funktiota.
    """

    for kehys in ikkuna:
        for nappi in kehys:
            if nappi["vasen"] <= x <= nappi["oikea"]:
                if nappi["yla"] <= y <= nappi["ala"]:
                    funktio = nappi["toiminto"]
                    funktio()
                    return
    
def kaynnista():
    """
    Lukee klikkauksia ja tarkistaa osuiko klikkaus nappiin. Silmukkaa
    suoritetaan niin kauan kuin tilasanakirjassa oleva "kaynnissa" arvo on
    True. Mikäli piirto valittiin tehtäväksi ohjelman käynnistyksessä, 
    piirtää nappien alueet sekä klikkauspisteet näkyviin.
    """

    tila["kaynnissa"] = True
    if tila["piirto"]:
        nayta_ikkuna()
    while tila["kaynnissa"]:
        print(".", end="", flush=True)
        hiiri_x, hiiri_y = lue_klikkaus()
        if tila["piirto"]:
            t.up()
            t.setx(hiiri_x - LEVEYS / 2)
            t.sety(KORKEUS / 2 - hiiri_y)
            t.down()
            t.dot()
        tunnista_nappi(hiiri_x, hiiri_y, ikkuna)
        # lisätty jotta ohjelma ei pyöri liian nopeasti
        time.sleep(0.1)
    if tila["piirto"]:
        t.done()
        
def lopeta():
    """
    Asettaa tilasanakirjassa olevan lipun Falseksi, jolloin kaynnista-funktiossa
    pyörivä pääsilmukka katkeaa ja ohjelma päättyy.
    """
    
    tila["kaynnissa"] = False
    
def nayta_ikkuna():
    """
    Piirtää kuvan ikkunasta turtlella. 
    """
    
    t.up()
    t.setx(-1 * LEVEYS / 2)
    t.sety(KORKEUS / 2)
    t.down()
    t.forward(LEVEYS)
    t.right(90)
    t.forward(KORKEUS)
    t.right(90)
    t.forward(LEVEYS)
    t.right(90)
    t.forward(KORKEUS)
    t.right(90)
    for kehys in ikkuna:
        for nappi in kehys:
            t.up()
            t.setx(nappi["vasen"] - LEVEYS / 2)
            t.sety(KORKEUS / 2 - nappi["yla"])
            t.down()
            t.forward(NAPPI_LEVEYS)
            t.right(90)
            t.forward(NAPPI_KORKEUS)
            t.right(90)
            t.forward(NAPPI_LEVEYS)
            t.right(90)
            t.forward(NAPPI_KORKEUS)
            t.right(90)
    
try:
    if sys.argv[1].lower() in ["-p", "--piirto"]:
        tila["piirto"] = True
except IndexError:
    pass
        
    
    
    