from turtle import *

def piirra_nelio(sivu, x, y):
    # tähän funktio joka piirtää neliön
    # joko punaisena tai sinisenä riippuen
    # siitä onko aloituspisteen x-koordinaatti
    # positiivinen (sininen) vai negativiinen
    # (punainen)
    
    if x >= 0:
        color("blue")
    else:
        color("red")
        
    begin_fill()
    up()
    goto(x, y)
    down()
    forward(sivu)
    left(90)
    forward(sivu)
    left(90)
    forward(sivu)
    left(90)
    forward(sivu)
    left(90)
    end_fill()
    up()
    
piirra_nelio(40, -100, 100)
piirra_nelio(60, 100, -100)
piirra_nelio(100, -50, -20)
piirra_nelio(80, 90, 30)
done()
