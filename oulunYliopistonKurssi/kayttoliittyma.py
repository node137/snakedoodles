import ikkunasto as ik

def lopeta():
    ik.lopeta()

def luo_ikkuna():
    ikkuna = ik.luo_ikkuna("Kokoelmaohjelma 0.1 alpha")
    nappikehys = ik.luo_kehys(ikkuna, ik.VASEN)
    kokoelmakehys = ik.luo_kehys(ikkuna, ik.VASEN)
    latausnappi = ik.luo_nappi(nappikehys, "Lataa", lataa_kokoelma)
    rakennusnappi = ik.luo_nappi(nappikehys, "Rakenna", rakenna_kokoelma)
    tallennusnappi = ik.luo_nappi(nappikehys, "Tallenna", tallenna_kokoelma)
    ik.luo_vaakaerotin(nappikehys, 5)
    lisaysnappi = ik.luo_nappi(nappikehys, "Lisää", lisaa)
    poistonappi = ik.luo_nappi(nappikehys, "Poista", poista)
    muokkausnappi = ik.luo_nappi(nappikehys, "Muokkaa", muokkaa)
    ik.luo_vaakaerotin(nappikehys, 5)
    lopetusnappi = ik.luo_nappi(nappikehys, "Lopeta", lopeta)
    kokoelmalaatikko = ik.luo_listalaatikko(kokoelmakehys)
    ik.kaynnista()

if __name__ == "__main__":
    #lahde, kohde = lue_argumentit(sys.argv)
    try:
        luo_ikkuna()
    except KeyboardInterrupt:
        print("Ohjelma keskeytettiin, kokoelmaa ei tallennettu")
