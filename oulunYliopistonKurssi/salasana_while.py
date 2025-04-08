def kysy_salasana():
    while True:
        salasana = input("Kirjoita salasana: ")
        if len(salasana) >= 8:
            return salasana
        print("Salasanan tulee olla vähintään 8 merkkiä pitkä")
print(kysy_salasana())
