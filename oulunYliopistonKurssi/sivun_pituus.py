import math 

def laske_sivun_pituus(hypotenuusa):
    kateetti = hypotenuusa /  math.sqrt(2)
    return kateetti

x = float(input("Anna tasakylkisen kolmion hypotenuusan pituus: "))
print("Kylkien pituus: ", round(laske_sivun_pituus(x),4))
