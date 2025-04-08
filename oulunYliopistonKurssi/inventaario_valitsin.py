def valitse_lukumaara(inventaario):
    lukumaara = int(inventaario[1])
    return lukumaara
inventaario = [("aasi", 12), ("muumimuki", 1), ("varsikirves", 4)]
inventaario.sort(key=valitse_lukumaara, reverse=True)
# kirjoita tähän rivi joka järjestää inventaarion kappalelukumäärien mukaan laskevassa järjestyksessä
print(inventaario)

