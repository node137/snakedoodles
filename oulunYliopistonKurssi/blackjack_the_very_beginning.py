def ylitys(summa):
    # ehtolause tähän
    if summa > 21:
        return True
    else:
        return False

summa = int(input("Anna käsikorttien summa: "))
if ylitys(summa):
    print("Hävisit")
else:
    print("Et hävinnyt, ainakaan vielä...")