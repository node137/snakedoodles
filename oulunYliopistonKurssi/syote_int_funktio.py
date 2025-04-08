""" 
This module performs functions of user inputs. 
"""
def pyyda_syote(pyynto, virheviesti):
    """
    Kysyy käyttäjältä kokonaislukua käyttäen kysymyksenä parametrina annettua
    merkkijonoa. Virheellisen syötteen kohdalla käyttäjälle näytetään toisena
    parametrina annettu virheilmoitus. Käyttäjän antama kelvollinen syöte
    palautetaan kokonaislukuna.
    
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
            return syote
luku = pyyda_syote(
    "Anna kokonaisluku: ",
    "Et antanut kokonaislukua"
)
print(f"Annoit kokonaisluvun {luku}! Nohevaa toimintaa!")
hemulit = pyyda_syote(
    "Montako hemulia mahtuu muumitaloon? ",
    "Tämä ei ollut kelvollinen hemulien lukumäärä!"
)
print(f"Muumitaloon mahtuu {hemulit} hemulia")
