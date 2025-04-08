""" 
This module keeps track of voting results. 
"""

verouudistus = {
    "jaa": 0,
    "ei": 0,
    "eos": 0,
    "virhe": 0
}
nalle_puh_presidentiksi = {
    "jaa": 12,
    "ei": 0,
    "eos": 5,
    "virhe": 4
}

def aanesta(vaalitulos_sanakirja):
    """
    Adds the wote to given election dictionary
    
    Args: 
        vaalitulos_sanakirja(dictionary): the dictionary to which 
            the vote is added
    """
    if vaalitulos_sanakirja == verouudistus:
        print("Suoritetaanko verouudistus?")
    else:
        print("Nalle Puh presidentiksi?")
    aani = input(
        "Anna äänesi, vaihtoehdot ovat: \n"
        "jaa, ei, eos\n"
    ).strip().lower()
    try:
        # haetaan sanakirjasta avain ja kasvatetaan ko. avaimen arvoa yhdellä
        vaalitulos_sanakirja[aani] += 1
    except KeyError:
        #arvoa ei löydy, kasvatetaan avaimen virhe arvoa yhdellä
        vaalitulos_sanakirja["virhe"] += 1

def nayta_tulokset(vaalitulostilanne_sanakirja):
    """
    Prints the results of the given election dictionary dictionary
    
    Args: 
        vaalitulostilanne_sanakirja(dictionary): the dictionary of which
            the voting results are being printed.
    """
    jaa = vaalitulostilanne_sanakirja["jaa"]
    ei = vaalitulostilanne_sanakirja["ei"]
    eos = vaalitulostilanne_sanakirja["eos"]
    virhe = vaalitulostilanne_sanakirja["virhe"]
    print(
        f"Jaa  : {'#' * jaa}\n"
        f"Ei   : {'#' * ei}\n"
        f"Eos  : {'#' * eos}\n"
        f"Virhe: {'#' * virhe}\n"
    )

aanesta(verouudistus)
nayta_tulokset(verouudistus)
aanesta(nalle_puh_presidentiksi)
nayta_tulokset(nalle_puh_presidentiksi)
