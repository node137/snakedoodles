viikko = ["maanantai", "tiistai", "keskiviikko", "torstai", "torstai", "perjantai", "lauantai", "sunnuntai"]
print(f"Viikossa on {len(viikko)} päivää: ")
print(", ".join(viikko))
poistopaiva = input("Minkä viikonpäivän haluat poistaa: ").lower()
if poistopaiva in viikko:
    viikko.remove(poistopaiva)
    print(f"Poistettu paiva on {poistopaiva}. Jätit viikkoosi seuraavat päivät:")
    print(", ".join(viikko))
    print(f"Viikossa on {len(viikko)} päivää: ")
else:
    print(f"Poistettava päivä {poistopaiva} ei ole viikonpäivä")
print("Tämä valinta on tyypillinen erityisesti paranormaaleista mielenhäiriöistä kärsiville yksilöille")


#vaihtoehtoinen tapa: 
viikko = ["maanantai", "tiistai", "keskiviikko", "torstai", "perjantai", "lauantai", "sunnuntai"]
print(f"Viikossa on {len(viikko)} päivää: ")
print(", ".join(viikko))
poisto = input("Minkä viikonpäivän haluat poistaa: ").lower()
try:
    viikko.remove(poisto)
except ValueError:
    print("Päivää ei ole.")
    print("Olemattomien päivien valinta on tyypillistä vainoharhaisille yksilöille")
else:
    print("Jätit viikkoosi seuraavat päivät:")
    print(", ".join(viikko))
    print("Tämä valinta on tyypillinen erityisesti paranormaaleista mielenhäiriöistä kärsiville yksilöille")


# listalta poisto luupissa, tietyn ehdon perusteella (poistaa kaikki ehdot täyttävät arvot, ei ainoastaan ensimmäistä)

elukoita = ["koira", "kissa", "aasi", "orava", "apina", "mursu", "laama"]
print(", ".join(elukoita))

for elain in elukoita[:]:
    if elain.startswith("a"):
        print(f"Poistetaan listalta {elain}")
        elukoita.remove(elain)
print(", ".join(elukoita))

