def laske_nopeus(matka, aika):
    nopeus = matka / aika
    return nopeus

try:     
    metrit = float(input("Anna auton kulkema matka (m): "))
    sekunnit = float(input("Anna matkaan kulunut aika (s):"))
except ValueError:
    print("Vähemmän donitseja, enemmän puhtaita numeroita.")
else:
    laskettu_nopeus = laske_nopeus(metrit/1000, sekunnit/3600)
    print(
        f"{metrit:.2f} metriä {sekunnit:.2f} sekunnissa kulkeneen auton "
        f"nopeus on {laskettu_nopeus:.2f} km/h."
    )
