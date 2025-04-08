import json
import nuuskija

import ikkunasto as ik

PER_SIVU = 5

EI_VALITTU = 0
LISAA = 1
MUOKKAA = 2

komponentit = {
    "laatikko": [],
    "levylomake": None,
    "lomake_artisti": None,
    "lomake_albumi": None,
    "lomake_kpl_n": None,
    "lomake_kesto": None,
    "lomake_julkaisuvuosi": None,
}

tila = {
    "kokoelma": [],
    "toiminto": EI_VALITTU,
    "valittu": None
}

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

def tarkista_kesto(kesto):
    return kesto

def lataa_kokoelma(tiedosto):

    try:
        with open(tiedosto) as lahde:
            tila["kokoelma"] = json.load(lahde)
    except (IOError, json.JSONDecodeError):
        print("Tiedoston avaaminen ei onnistunut. Aloitetaan tyhjällä kokoelmalla")

def tallenna_kokoelma(tiedosto):
    try:
        with open(tiedosto, "w") as kohde:
            json.dump(tila["kokoelma"], kohde)
    except IOError:
        print("Kohdetiedostoa ei voitu avata. Tallennus epäonnistui")

def lue_tiedot_lomakkeesta(levy):
    levy["artisti"] = ik.lue_kentan_sisalto(komponentit["lomake_artisti"])
    levy["albumi"] = ik.lue_kentan_sisalto(komponentit["lomake_albumi"])
    try:
        levy["kpl_n"] = int(ik.lue_kentan_sisalto(komponentit["lomake_kpl_n"]))
    except ValueError:
        ik.avaa_viesti_ikkuna("Virhe tiedoissa",
            "Kappaleiden lukumäärän on oltava kokonaisluku",
            virhe=True
        )
        return None

    try:
        levy["kesto"] = tarkista_kesto(ik.lue_kentan_sisalto(komponentit["lomake_kesto"]))
    except ValueError:
        ik.avaa_viesti_ikkuna("Virhe tiedoissa",
            "Keston on oltava muodossa HH:MM:SS",
            virhe=True
        )
        return None

    try:
        levy["julkaisuvuosi"] = int(ik.lue_kentan_sisalto(komponentit["lomake_vuosi"]))
    except ValueError:
        ik.avaa_viesti_ikkuna("Virhe tiedoissa",
            "Julkaisuvuoden on oltava kokonaisluku",
            virhe=True
        )
        return None

    return levy

def lisaa(kokoelma):
    levy = lue_tiedot_lomakkeesta({})
    if levy:
        kokoelma.append(levy)
        return True
    return False

def kirjoita_tiedot_lomakkeeseen():
    valittu, sisalto = ik.lue_valittu_rivi(komponentit["laatikko"])
    levy = tila["kokoelma"][valittu]
    ik.kirjoita_tekstikenttaan(komponentit["lomake_artisti"], levy["artisti"])
    ik.kirjoita_tekstikenttaan(komponentit["lomake_albumi"], levy["albumi"])
    ik.kirjoita_tekstikenttaan(komponentit["lomake_kpl_n"], levy["kpl_n"])
    ik.kirjoita_tekstikenttaan(komponentit["lomake_kesto"], levy["kesto"])
    ik.kirjoita_tekstikenttaan(komponentit["lomake_vuosi"], levy["julkaisuvuosi"])
    return valittu

def muokkaa(kokoelma, indeksi):
    levy = lue_tiedot_lomakkeesta(kokoelma[indeksi].copy())
    if levy:
        kokoelma[indeksi] = levy
        return True
    return False

def poista():
    valittu, sisalto = ik.lue_valittu_rivi(komponentit["laatikko"])
    if valittu is not None:
        print(f"kokoelma: {tila["kokoelma"]}")
        print(f"valittu: {valittu}")
        tila["kokoelma"].pop(valittu)
        ik.poista_rivi_laatikosta(komponentit["laatikko"], valittu)

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

def muotoile_rivi(levy):
    return (
        #f"{i:2}. "
        f"{levy['artisti']} - {levy['albumi']} ({levy['julkaisuvuosi']}) "
        f"[{levy['kpl_n']}] [{levy['kesto'].lstrip('0:')}]"
    )

def tulosta(kokoelma):
    for levy in kokoelma:
        ik.lisaa_rivi_laatikkoon(komponentit["laatikko"], muotoile_rivi(levy))

def rakenna_kokoelma(kansio):
    try:
        tila["kokoelma"] = nuuskija.lue_kokoelma(kansio)
    except FileNotFoundError:
        print("Kansiota ei löytynyt")

def lue_argumentit(argumentit):
    if len(argumentit) >= 3:
        lahde = argumentit[1]
        kohde = argumentit[2]
        return lahde, kohde
    elif len(argumentit) == 2:
        lahde = argumentit[1]
        return lahde, lahde
    
    return None, None

def avaa_latausikkuna():
    polku = ik.avaa_tiedostoikkuna("Valitse kokoelmatiedosto (JSON)")
    lataa_kokoelma(polku)
    tulosta(tila["kokoelma"])

def avaa_rakennusikkuna():
    polku = ik.avaa_hakemistoikkuna("Valitse kokoelman juurikansio")
    rakenna_kokoelma(polku)
    tulosta(tila["kokoelma"])

def avaa_tallennusikkuna():
    polku = ik.avaa_tallennusikkuna("Valitse kohdetiedosto (JSON)")
    tallenna_kokoelma(polku)

def avaa_lisayslomake():
    ik.nayta_ali_ikkuna(komponentit["levylomake"], "Lisää levy")
    tila["toiminto"] = LISAA

def avaa_muokkauslomake():
    paikka = kirjoita_tiedot_lomakkeeseen()
    ik.nayta_ali_ikkuna(komponentit["levylomake"], "Muokkaa levyä")
    tila["toiminto"] = MUOKKAA
    tila["valittu"] = paikka

def tallenna_lomake():
    if tila["toiminto"] == LISAA:
        onnistui = lisaa(tila["kokoelma"])
        paikka = len(tila["kokoelma"]) - 1
    elif tila["toiminto"] == MUOKKAA:
        paikka = tila["valittu"]
        onnistui = muokkaa(tila["kokoelma"], paikka)
        if onnistui:
            ik.poista_rivi_laatikosta(komponentit["laatikko"], paikka)
            tila["valittu"] = None
    else:
        return

    if onnistui:
        ik.lisaa_rivi_laatikkoon(
            komponentit["laatikko"], muotoile_rivi(tila["kokoelma"][paikka]), paikka
        )
        ik.tyhjaa_kentan_sisalto(komponentit["lomake_artisti"])
        ik.tyhjaa_kentan_sisalto(komponentit["lomake_albumi"])
        ik.tyhjaa_kentan_sisalto(komponentit["lomake_kpl_n"])
        ik.tyhjaa_kentan_sisalto(komponentit["lomake_kesto"])
        ik.tyhjaa_kentan_sisalto(komponentit["lomake_vuosi"])
        ik.piilota_ali_ikkuna(komponentit["levylomake"])
        tila["toiminto"] = EI_VALITTU

def lopeta():
    ik.lopeta()

def luo_ikkuna():

    # Pääikkunan luonti
    ikkuna = ik.luo_ikkuna("Kokoelmaohjelma 0.1 alpha")
    nappikehys = ik.luo_kehys(ikkuna, ik.VASEN)
    kokoelmakehys = ik.luo_kehys(ikkuna, ik.VASEN)
    ik.luo_nappi(nappikehys, "Lataa", avaa_latausikkuna)
    ik.luo_nappi(nappikehys, "Rakenna", avaa_rakennusikkuna)
    ik.luo_nappi(nappikehys, "Tallenna", avaa_tallennusikkuna)
    ik.luo_vaakaerotin(nappikehys, 5)
    ik.luo_nappi(nappikehys, "Lisää", avaa_lisayslomake)
    ik.luo_nappi(nappikehys, "Poista", poista)
    ik.luo_nappi(nappikehys, "Muokkaa", avaa_muokkauslomake)
    ik.luo_vaakaerotin(nappikehys, 5)
    ik.luo_nappi(nappikehys, "Lopeta", lopeta)
    komponentit["laatikko"] = ik.luo_listalaatikko(kokoelmakehys)

    # Ali-ikkunan luonti
    levylomake = ik.luo_ali_ikkuna("Levyn tiedot")
    kenttakehys = ik.luo_kehys(levylomake, ik.YLA)
    nappikehys = ik.luo_kehys(levylomake, ik.YLA)
    ohjekehys = ik.luo_kehys(kenttakehys, ik.VASEN)
    syotekehys = ik.luo_kehys(kenttakehys, ik.VASEN)
    ik.luo_tekstirivi(ohjekehys, "Artisti")
    komponentit["lomake_artisti"] = ik.luo_tekstikentta(syotekehys)
    ik.luo_tekstirivi(ohjekehys, "Albumi")
    komponentit["lomake_albumi"] = ik.luo_tekstikentta(syotekehys)
    ik.luo_tekstirivi(ohjekehys, "Kpl N")
    komponentit["lomake_kpl_n"] = ik.luo_tekstikentta(syotekehys)
    ik.luo_tekstirivi(ohjekehys, "Kesto (HH:MM:SS)")
    komponentit["lomake_kesto"] = ik.luo_tekstikentta(syotekehys)
    ik.luo_tekstirivi(ohjekehys, "Julkaisuvuosi")
    komponentit["lomake_vuosi"] = ik.luo_tekstikentta(syotekehys)
    ik.luo_nappi(nappikehys, "Tallenna", tallenna_lomake)
    ik.piilota_ali_ikkuna(levylomake)
    komponentit["levylomake"] = levylomake
    ik.kaynnista()

if __name__ == "__main__":
    #lahde, kohde = lue_argumentit(sys.argv)
    try:
        luo_ikkuna()
    except KeyboardInterrupt:
        print("Ohjelma keskeytettiin, kokoelmaa ei tallennettu")
