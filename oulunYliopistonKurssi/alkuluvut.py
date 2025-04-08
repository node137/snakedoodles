""" 
This module performs functions of user inputs. 
"""
def pyyda_syote(pyynto, virheviesti):
    """
    Kysyy käyttäjältä kokonaislukua käyttäen kysymyksenä parametrina annettua
    merkkijonoa. Virheellisen syötteen kohdalla käyttäjälle näytetään toisena
    parametrina annettu virheilmoitus. Käyttäjän antama kelvollinen syöte
    palautetaan kokonaislukuna. Hyväksyy vain luvut jotka ovat suurempia kuin 1.
    
    Args: 
        pyynto (string): käyttäjälle esitettävä pyyntö.
        virheviesti (string): käyttäjälle esitettävä virheviesti virheen sattuessa.
    Returns: 
        int: tarkistettu, käyttäjän kokonaislukuna antama syöte.
    
    """
    while True:
        try:
            syote = int(input(pyynto))
        except ValueError:
            print(virheviesti)
        else:
            if syote < 2:
                print(virheviesti)
            else:
                return syote

def tarkista_alkuluku(tarkastettava_arvo):
    """
    Tarkistaa onko parametrina annettu luku alkuluku. Palauttaa False jos luku ei
    ole alkuluku; jos luku on alkuluku palautetaan True
    
    Args: 
        tarkastettava_arvo (int): tarkastettava arvo
    Returns: 
        boolean: onko luku slkuluku.
        
    """        
    if tarkastettava_arvo < 2:
        return False
    for i in range(2, int(tarkastettava_arvo ** 0.5) + 1):
        if tarkastettava_arvo % i == 0:
            return False
    return True
luku = pyyda_syote(
    "Anna kokonaisluku, joka on suurempi kuin 1: ",
    "Pieleen meni :'(."
)
if tarkista_alkuluku(luku):
    print("Kyseessä on alkuluku.")
else:
    print("Kyseessä ei ole alkuluku.")
