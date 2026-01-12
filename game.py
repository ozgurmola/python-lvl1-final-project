import pgzrun
import random

#Karakterler
#number = 4
#screen.draw.text(str(number))

TITLE="SELAM"
WIDTH = 500
HEIGHT= 500
FPS=30

hero = Actor ("hero") 
final_boss = Actor ("final_boss")
bg =Actor ("lanetli_orman") 
 


def draw():
    bg.draw()
    hero.draw()









#düşman oluşturma
#enemies = []
#for i in range(5):
    
    #enemy = Actor("kurt", topleft = (x, y))
    #enemy.health = random.randint(10, 20)
    #enemy.attack = random.randint(5, 10)
    #enemies.append(enemy)

pgzrun.go()
