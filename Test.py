from graphics import *
import random


#Este programa se trata de monstruos creados con el rectangulo de la clase graphics con una cantidad de hp aleatoria, 
#alrededor de 1 a 10, estos van a apaterecer tambien en la pantalla aleatoriamente 
# y el jugador tiene que darle la cantidad de clicks que el monstruo tenga en su hp.
#  Este juego tiene un timer y va a ver al final cuantos pudiste derrotar cuando se acabe el timer.

win=GraphWin("Click hunt",600,600)


#MpositionX= random.randint(1,10)
for i in range(1):
    MpositionX= random.randint(30,251)
    MpositionY= random.randint(250,300)
    Mposition=Rectangle(Point(MpositionX,MpositionY),Point(MpositionY,MpositionX))
    Mposition.setFill(color_rgb(0,120,0))
    Mposition.draw(win)
    
win.getMouse()
win.close()




#win.getMouse()
#win.close()