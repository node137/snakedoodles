from turtle import *

def piirra_spiraali(vari, kaarien_lkm, alkusade, sateen_kasvu, viivan_paksuus=1):
    color(vari)
    pensize(viivan_paksuus) 
    for i in range(kaarien_lkm):
        #down()
        circle(alkusade, 90)
        alkusade += sateen_kasvu
        #up() 
    
piirra_spiraali("black", 20, 10, 3)
piirra_spiraali("red", 10, 20, 4, 3)
piirra_spiraali("blue", 10, -20, -4, 3)
done()
