#import kirjasto
import ikkunasto as kirjasto

def tulosta_aasi():
    print("aasi")
    
def tulosta_hemuli():
    print("hemuli")

ikkuna = kirjasto.luo_ikkuna("testi")
kehys = kirjasto.luo_kehys(ikkuna)
kirjasto.luo_nappi(kehys, "nappi 1", tulosta_aasi)
kirjasto.luo_nappi(kehys, "nappi 2", tulosta_hemuli)
kirjasto.luo_nappi(kehys, "lopeta", kirjasto.lopeta)
kirjasto.kaynnista()
print("terve, ja kiitos kaloista")