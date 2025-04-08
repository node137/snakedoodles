""" 
This module performs functions of some serious ninja actions. 
"""
def tutki_ruutu(merkkijono, tarkastettava):
    """
    Funktio tutkii ruudun - jos siellä on ninja, se palauttaa True.
    
    Args:
        merkkijono (string): ruudussa oleva merkki (merkkijono)
        tarkastettava (string): ruudun sisällöstä etsittävä merkki
    Return:
        (boolean): if square contains given value
            returns True, if not, returns False
    """
    if merkkijono == tarkastettava:
        return True
    return False
def laske_ninjat(x, y, huoneessa):
    """
    Laskee annetussa huoneessa yhden ruudun ympärillä olevat ninjat ja palauttaa
    niiden lukumäärän. Funktio toimii sillä oletuksella, että valitussa ruudussa ei
    ole ninjaa - jos on, sekin lasketaan mukaan.
    
    Args:
        x (int): valitun ruudun x-koordinaatti (kokonaisluku)
        y (int): valitun ruudun y-koordinaatti (kokonaisluku)
        huoneessa (list): huonetta kuvaava rakenne (lista, joka 
            sisältää listoja jotka sisältävät yksittäisiä merkkejä)
    Returns:
        ninja_count (int): ruutua ympäröivien ninjojen kokonaismäärä
    """
    ninja_count = 0
    x_leveys = len(huoneessa[0])
    y_korkeus = len(huoneessa)
    suuntakoordinaatit = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1), (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]
    for sx, sy in suuntakoordinaatit:
        suunta_x = x + sx
        suunta_y = y + sy
        # Tarkistetaan, että suunta_x ja suunta_y ovat huoneen sisällä
        if 0 <= suunta_x < x_leveys and 0 <= suunta_y < y_korkeus:
            if tutki_ruutu(huoneessa[suunta_y][suunta_x],'N'):
                ninja_count += 1
    return ninja_count
#   for y, rivi in enumerate(huoneessa):
#       for x, avain in enumerate(rivi):
#           if tutki_ruutu(avain, 'N'):
#               ninja_count += 1
#   return ninja_count
# Pääohjelma:
huone = [
    ['N', ' ', ' ', ' ', ' '],
    ['N', 'N', 'N', 'N', ' '],
    ['N', ' ', 'N', ' ', ' '],
    ['N', 'N', 'N', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ']
]
print(" ", "- " * 5)
for rivi in huone:
    print("|", " ".join(rivi), "|")
print(" ", "- " * 5)
x_param = int(input("Anna x-koordinaatti: "))
y_param = int(input("Anna y-koordinaatti: "))
print(f"Ruutua ympäröi {laske_ninjat(x_param, y_param, huone)} ninjaa")
