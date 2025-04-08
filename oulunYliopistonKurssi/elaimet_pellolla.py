ELAIMET = {
    "a": "aasi",
    "k": "koira",
    "@": "kissa",
    "h": "hemuli",
    "l": "lammas"
}

def tutki_ruutu(merkkijono, rivinro, sarakenro):
    """
    Funktio tutkii ruudun - jos siellä on eläin, se tulostaa eläimen sijainnin sekä nimen.
    
    Args:
        merkkijono (sttring): ruudussa oleva merkki (merkkijono)
        sarakenro (int): rivin numero
        rivinro (int): sarakkeen numero
    """    
    if merkkijono in ELAIMET:
        elain = ELAIMET[merkkijono]
        print(f"Ruudusta ({sarakenro}, {rivinro}) löytyy {elain}")

def tutki_kentta(pelikentta):
    """
    Funktio tutkii kentän sisällön käymällä sen kokonaan läpi kutsuen tutki_ruutu-funktiota
    jokaiselle kentän sisällä olevalle alkiolle.
    
    Args: 
        pelikentta (list): kenttää kuvaava 2-ulotteinen lista
    """
    for y, rivi in enumerate(pelikentta):
        for x, avain in enumerate(rivi):
            tutki_ruutu(avain, y, x)

pelto = [
    [" ", "a", " ", " ", "l"],
    [" ", "k", "@", "k", " "],
    ["h", " ", "a", "k", " "]
]

tutki_kentta(pelto)
