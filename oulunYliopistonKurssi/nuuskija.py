import os
import time
import tinytag

def parsi_kestotiedot(kokoelma):
    for levy in kokoelma:
        levy["kesto"] = time.strftime("%H:%M:%S", time.gmtime(sum(levy["kestot"])))
        levy["kpl_n"] = len(levy["kestot"])
        levy.pop("kestot")

def lue_kansio(kansio, kokoelma):
    print("Avataan kansio:", kansio)
    sisalto = os.listdir(kansio)
    for nimi in sisalto: 
        polku = os.path.join(kansio, nimi)
        if os.path.isdir(polku):
            lue_kansio(polku, kokoelma)
        else:
            try:   
                lue_tiedot(polku, kokoelma)
            except tinytag.TinyTagException:
                print("Ohitetaan", nimi)

def lue_tiedot(tiedosto, kokoelma):
    tiedot = tinytag.TinyTag.get(tiedosto)
    albumi = tiedot.album
    artisti = tiedot.artist
    vuosi = tiedot.year
    kesto = tiedot.duration 
    for levy in kokoelma: 
        if levy["artisti"].lower() == artisti.lower() and levy["albumi"].lower() == albumi.lower():
            levy["kestot"].append(kesto)
            break
    else:
        kokoelma.append({
            "artisti": artisti,
            "albumi": albumi,
            "kestot": [kesto],
            "julkaisuvuosi": vuosi
        })

def lue_kokoelma(kansio):
    kokoelma = []
    lue_kansio(kansio, kokoelma)
    parsi_kestotiedot(kokoelma)
    return kokoelma

if __name__ == "__main__":
    kokoelma = []
    lue_kansio("E:/Music", kokoelma)
    parsi_kestotiedot(kokoelma)
    for levy in kokoelma:
        print(levy)
