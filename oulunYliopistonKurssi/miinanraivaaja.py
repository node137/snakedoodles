""" 
This module performs functions of a minefield game. 
"""

TULOSTUKSET = {
    "ulkona": "Antamasi ruutu on kentän ulkopuolella.",
    "nurkassa": "Antamasi ruutu on kentän nurkassa.",
    "laidalla": "Antamasi ruutu on kentän laidalla.",
    "keskellä": "Antamasi ruutu on keskikentällä."
}

def sijainti_kentalla(x, y, leveys, korkeus):

    """
    Adds, subtracts, multiplies or divides two numbers 
    based on the given operation.
    The operation will be performed on the first number 
    using the second number.
    
    Args: 
        x (int): The x cordinate.
        y (int): The y cordinate.
        leveys (int): The width of the field.
        korkeus (int): The height of the field. 
    Returns: 
        string: key in the TULOSTUKSET dictionary, 
            which correspondes to the position in the field.
    """
    if x >= leveys or y >= korkeus or x < 0 or y < 0:
        avainsana = "ulkona"
    elif (x == 0 and y == 0) or (x == leveys-1 and y == 0):
        avainsana = "nurkassa"
    elif (x == leveys-1 and y == korkeus-1) or (y == korkeus-1 and x == 0):
        avainsana = "nurkassa"
    elif x == leveys-1 or y == korkeus-1 or x == 0 or y == 0:
        avainsana = "laidalla"
    else:
        avainsana = "keskellä"
    return avainsana

def tulosta_sijainti(sijainnin_avainsana):
    """ 
    Prints the position in the field.
    
    Args: 
        sijainnin_avainsana (int): The key of the position in the field.
    """
    print(TULOSTUKSET[sijainnin_avainsana])

kentan_leveys = int(input("Anna kentän leveys: "))
kentan_korkeus = int(input("Anna kentän korkeus: "))

if kentan_korkeus < 1 or kentan_leveys < 1:
    print("Noin pienelle kentälle ei mahdu ainuttakaan ruutua!")
else:
    x_koordinaatti = int(input("Anna x-koordinaatti: "))
    y_koordinaatti = int(input("Anna y-koordinaatti: "))
    tulosta_sijainti(
        sijainti_kentalla(x_koordinaatti, y_koordinaatti, kentan_leveys, kentan_korkeus))
