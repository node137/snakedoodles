def muotoile_heksaluvuksi(kokonaisluku, bittilkm):
    haluttu_pituus = bittilkm // 4
    heksaluku = hex(kokonaisluku).lstrip("0x").zfill(haluttu_pituus)
    return heksaluku

try: 
    muunnettava = int(input("Anna kokonaisluku: "))
    heksapituus = int(input("Anna heksaluvun pituus (bittien lukumäärä): "))
except ValueError:
    print("Kokonaisluku kiitos")
else:
    print(muotoile_heksaluvuksi(muunnettava, heksapituus))
