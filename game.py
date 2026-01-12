import pgzrun
import random

#Karakterler
#number = 4
#screen.draw.text(str(number))

TITLE="SELAM"
WIDTH = 1000
HEIGHT= 1050
FPS=30




hero = Actor ("hero") 
final_boss = Actor ("final_boss")
bg =Actor ("lanetli_orman") 

hero.health =100
hero.attack = 5

wolfs= []
count = random.randint(2, 7)
for i in range(count):
    x = random.randint(200, 800)
    y = random.randint(200, 800)
    enemy = Actor("kurt", (x, y))
    wolfs.append(enemy)


def draw():
    global wolfs
    bg.draw()
    hero.draw()
    for i in range(len(wolfs)):
        wolfs[i].draw()
    screen.draw.text("HP:", center=(25, 1000), color = 'white', fontsize = 40)
    screen.draw.text(str(hero.health), center=(75, 1000), color = 'white', fontsize = 40)
    screen.draw.text("AP:", center=(375, 1000), color = 'white', fontsize = 40)
    screen.draw.text(str(hero.attack), center=(425, 1000), color = 'white', fontsize = 40)
 




def update(dt):

    old_x = hero.x
    old_y = hero.y
    if keyboard.left and hero.x > 50:
        hero.x -= 5
    elif keyboard.right and hero.x < 950:
        hero.x += 5
    elif keyboard.up and hero.y > 50:
        hero.y -= 5
    elif keyboard.down and hero.y < 950:
        hero.y += 5




enemy_index = hero.collidelist(wolfs)
if enemy_index != -1:
    hero.x = old_x
    hero.y = old_y
    enemy = wolfs[enemy_index]
    enemy.health -= hero.attack
    hero.health -= enemy.attack
    if enemy.health <0:
        wolfs.pop(enemy_index)



pgzrun.go()

