""" 
This module performs functions of value checking. 
"""
def suodata_virhearvot(p_mittaukset, reuna_arvo):
    """
    Funktio suodattaa ja poistaa virheelliset alkiot listalta
    eli poistaa mittaustuloksista kaikki arvot, jotka ylittävät reuna-arvon. 
    
    Args:
        p_mittaukset (list): suodatettava lista mittaustuloksista, sisältää
            liukulukuarvoja
        reuna_arvo (float): reuna-arvo, joka määrittää poistettavat alkiot
    """
    for mittaus in p_mittaukset[:]:
        if mittaus > reuna_arvo:
            p_mittaukset.remove(mittaus)

# Pääohjelma:
mittaukset = [12.2, 54.2, 42345.2, 23534.1, 55.7, 8982.4]
suodata_virhearvot(mittaukset, 8000)
print(mittaukset)
