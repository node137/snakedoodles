import math

def muunna_xy_koordinaateiksi(kulma, pituus):  
    x_koordinaatti = int(round(pituus * math.cos(kulma)))
    y_koordinaatti = int(round(pituus * math.sin(kulma)))
    return x_koordinaatti, y_koordinaatti

x = float(input("Anna kulma radiaaneina: "))
y = float(input("Anna osoitinvektorin pituus: "))
x_piste, y_piste = muunna_xy_koordinaateiksi(x, y)
print("Koordinaatit (x, y): (", x_piste, ", ", y_piste, ")")
