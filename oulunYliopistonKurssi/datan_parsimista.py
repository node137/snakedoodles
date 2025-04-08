"""
    This datan_parsimista.pmodule contains functions to handle data from files
"""

def nayta_tulokset(tiedosto):
    """
    Funktio lukee tiedostoa, jossa on kullakin datarivillä
    seuraavat tiedot, tässä järjestyksessä:
    pelaajan 1 nimi, pelaajan 2 nimi, pelaajan 1 pisteet, pelaajan 2 pisteet
    Tämä data luetaan listaksi
    
    Args:
        tiedosto (string): name of the file to ne read
    """
    try:
        with open(tiedosto) as lahde:
            for rivi in lahde.readlines():
                osat = rivi.split(",")
                for i, osa in enumerate(osat):
                    osat[i] = osa.strip()
                pelaaja1 = osat[0]
                pelaaja2 = osat[1]
                pelaaja1_pisteet = osat[2]
                pelaaja2_pisteet = osat[3]
                print(f"{pelaaja1} {pelaaja1_pisteet} - {pelaaja2_pisteet} {pelaaja2}")
    except IOError:
        print("Tiedoston avaaminen ei onnistunut.")  
nayta_tulokset("hemulicup.csv")
