inventaario = [("aasi", 12), ("muumimuki", 1), ("varsikirves", 4)]

def hae_lukumaara(tuote):
    return tuote[1]
    
for nimi, kpl in inventaario:
    print(f"Varastossa on {kpl} x {nimi}")
# kirjoita tähän rivi joka järjestää inventaarion kappalelukumäärien mukaan laskevassa järjestyksessä
inventaario.sort(key=hae_lukumaara, reverse=True)
print(inventaario)





