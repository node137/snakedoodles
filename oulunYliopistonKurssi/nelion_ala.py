def laske_nelion_ala(sivun_pituus):
    # neliötehtävän funktion koodi
    nelion_ala = sivun_pituus ** 2
    return nelion_ala

x = float(input("Anna neliön sivun pituus: "))
print("Neliön pinta-ala: ", round(laske_nelion_ala(x),4))
