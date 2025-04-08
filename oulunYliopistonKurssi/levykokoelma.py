PER_SIVU = 20

def kysy_luku(kysymys):
    while True:
        try:
            luku = int(input(kysymys))
        except ValueError:
            print("Arvon tulee olla kokonaisluku")
        else:
            return luku

def jarjesta(kokoelma):
    print("Valitse kenttä jonka mukaan kokoelma järjestetään syöttämällä kenttää vastaava numero")
    print("1 - artisti")
    print("2 - levyn nimi")
    print("3 - kappaleiden määrä")
    print("4 - levyn kesto")
    print("5 - julkaisuvuosi")
    kentta = input("Valitse kenttä (1-5): ")
    jarjestys = input("Järjestys; (l)askeva vai (n)ouseva: ").lower()
    if jarjestys == "l":
        kaanna = True
    else:
        kaanna = False
    if kentta == "1":
        kokoelma.sort(key=valitse_artisti, reverse=kaanna)
    elif kentta == "2":
        kokoelma.sort(key=valitse_albumi, reverse=kaanna)
    elif kentta == "3":
        kokoelma.sort(key=valitse_kpl_n, reverse=kaanna)
    elif kentta == "4":
        kokoelma.sort(key=valitse_kesto, reverse=kaanna)
    elif kentta == "5":
        kokoelma.sort(key=valitse_julkaisuvuosi, reverse=kaanna)
    else:
        print("Kenttää ei ole olemassa")

def valitse_artisti(levy):
    return levy["artisti"]

def valitse_albumi(levy):
    return levy["albumi"]

def valitse_kpl_n(levy):
    return levy["kpl_n"]

def valitse_kesto(levy):
    return levy["kesto"]

def valitse_julkaisuvuosi(levy):
    return levy["julkaisuvuosi"]

def kysy_aika(kysymys):
    while True:
        osat = input(kysymys).split(":")
        if len(osat) == 3:
            h, min, s = osat
        elif len(osat) == 2:
            min, s = osat
            h = "0"
        else:
            print("Anna aika muodossa tunnit:minuutit:sekunnit tai minuutit:sekunnit")
            continue

        try:
            h = int(h)
            min = int(min)
            s = int(s)
        except ValueError:
            print("Aikojen on oltava kokonaislukuja")
            continue

        if not (0 <= min <= 59):
            print("Minuuttien on oltava välillä 0-59")
            continue
        if not(0 <= s <= 59):
            print("Sekuntien on oltava välillä 0-59")
            continue
        if h < 0:
            print("Tuntien on oltava positiivinen kokonaisluku")
            continue

        return f"{h}:{min:02}:{s:02}"


def lataa_kokoelma():
    """
    Luo testikokoelman. Palauttaa listan, joka sisältää viiden avain-arvo-parin
    sanakirjoja.
    Sanakirjan avaimet vastaavat seuraavia tietoja:
    "artisti" - artisti nimi
    "albumi" - levyn nimi
    "kpl_n" - kappaleiden määrä
    "kesto" - kesto
    "julkaisuvuosi" - julkaisuvuosi
    """

    kokoelma = [
        {
            "artisti": "Alcest",
            "albumi": "Kodama",
            "kpl_n": 6,
            "kesto": "0:42:15",
            "julkaisuvuosi": 2016
        },
        {
            "artisti": "Canaan",
            "albumi": "A Calling to Weakness",
            "kpl_n": 17,
            "kesto": "1:11:17",
            "julkaisuvuosi": 2002
        },
        {
            "artisti": "Deftones",
            "albumi": "Gore",
            "kpl_n": 11,
            "kesto": "0:48:13",
            "julkaisuvuosi": 2016
        },
        # katkaistaan tästä, koko esimerkin koodissa määritelty 8 lisää
    ]
    return kokoelma

def tallenna_kokoelma(kokoelma):
    """
    Tallentaa kokoelman, joskus tulevaisuudessa.
    """

    pass

def lisaa(kokoelma):
    print("Täytä lisättävän levyn tiedot. Jätä levyn nimi tyhjäksi lopettaaksesi")
    while True:
        levy = input("Levyn nimi: ")
        if not levy:
            break

        artisti = input("Artistin nimi: ")
        kpl_n = kysy_luku("Kappaleiden lukumäärä: ")
        kesto = kysy_aika("Kesto: ")
        vuosi = kysy_luku("Julkaisuvuosi: ")
        kokoelma.append({
            "artisti": artisti,
            "albumi": levy,
            "kpl_n": kpl_n,
            "kesto": kesto,
            "julkaisuvuosi": vuosi
        })
        print("Levy lisätty")

def poista(kokoelma):
    """
    Poistaa leven kokoelmasta, joskus tulevaisuudessa.
    """

    pass

def muotoile_sivu(rivit, sivu):
    for i, levy in enumerate(rivit, sivu * PER_SIVU + 1):
        print(
            f"{i:2}. "
            f"{levy['artisti']} - {levy['albumi']} ({levy['julkaisuvuosi']}) "
            f"[{levy['kpl_n']}] [{levy['kesto'].lstrip('0:')}]"
        )

#vaihtoehtoinen toteutus:
#def muotoile_sivu(rivit, sivu):
#    for i, levy in enumerate(rivit, sivu * PER_SIVU + 1):
#        print("{i:2}. {artisti} - {albumi} ({vuosi}) [{kpl_n}] [{kesto}]".format(
#            i=i,
#            artisti=levy["artisti"],
#            albumi=levy["albumi"],
#            kpl_n=levy["kpl_n"],
#            kesto=levy["kesto"].lstrip("0:"),
#            vuosi=levy["julkaisuvuosi"]
#        ))

def tulosta(kokoelma):
    tulostuksia = math.ceil(len(kokoelma) / PER_SIVU)
    for i in range(tulostuksia):
        alku = i * PER_SIVU
        loppu = (i + 1) * PER_SIVU
        muotoile_sivu(kokoelma[alku:loppu], i)
        if i < tulostuksia - 1:
            input("   -- paina enter jatkaaksesi tulostusta --")

kokoelma = lataa_kokoelma()
print("Tämä ohjelma ylläpitää levykokoelmaa. Voit valita seuraavista toiminnoista:")
print("(L)isää uusia levyjä")
print("(P)oista levyjä")
print("(J)ärjestä kokoelma")
print("(T)ulosta kokoelma")
print("(Q)uittaa")
while True:
    valinta = input("Tee valintasi: ").strip().lower()
    if valinta == "l":
        lisaa(kokoelma)
    elif valinta == "p":
        poista(kokoelma)
    elif valinta == "j":
        jarjesta(kokoelma)
    elif valinta == "t":
        tulosta(kokoelma)
    elif valinta == "q":
        break
    else:
        print("Valitsemaasi toimintoa ei ole olemassa")
tallenna_kokoelma(kokoelma)
