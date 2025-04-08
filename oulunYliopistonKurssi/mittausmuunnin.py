
YKSIKOT = {
    "in": (2.54, "cm"),
    "\"": (2.54, "cm"),
    "ft": (30.48, "cm"),
    "'": (30.48, "cm"),
    "yd": (0.9144, "m"),
    "mi": (1.609344, "km"),
    "oz": (28.349523125, "g"),
    "lb": (0.45359237, "kg"),
    "cp": (2.365882365, "dl"),
    "pt": (4.73176473, "dl"),
    "qt": (0.946352946, "l"),
    "gal": (3.785411784, "l")    
}


def muunna_si_yksikoksi(mittaus):
    arvo = mittaus["arvo"]
    yksikko = mittaus["yksikko"]    
    try:
        # monikon 1. alkio on kerroin
        si_arvo = arvo * YKSIKOT[yksikko][0] 
    except KeyError:
        mittaus["virheellinen"] = True
    else:
        # monikon 2. alkio on kohdeyksikkö
        mittaus["yksikko"] = YKSIKOT[yksikko][1]
        mittaus["arvo"] = si_arvo

def lue_mittaukset():
    print("Syötä mitatut arvot ja yksiköt välilyönnillä erotettuna. Tyhjä syöte lopettaa.")
    mittaukset = []
    while True:        
        syote = input("Anna mittaus: ").strip()
        try:
            arvo, yksikko = syote.split(" ")
            arvo = float(arvo)
        except ValueError:
            if not syote:
                return mittaukset
            print("Anna syötteet pyydetyssä muodossa.")
        else:
            mittaukset.append({
                "yksikko": yksikko,
                "arvo": arvo
            })

def tulosta_mittaukset(mittaukset):
    for mittaus in mittaukset:
        if mittaus.get("virheellinen"):
            print("virheellinen mittaus: {arvo:.3f} {yksikko}".format(**mittaus))
        else:
            print("{arvo:.3f} {yksikko}".format(**mittaus))

def paaohjelma():
    mittaukset = lue_mittaukset()
    for mittaus in mittaukset:
        muunna_si_yksikoksi(mittaus)
    
    tulosta_mittaukset(mittaukset)

try:
    paaohjelma()
except KeyboardInterrupt:
    print("Mittausten käsittely keskeytetty.")
