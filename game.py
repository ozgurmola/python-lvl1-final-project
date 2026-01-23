import pgzrun
import random

TITLE = "ARİNİN MACERALARI"
WIDTH = 1000
HEIGHT = 1000
FPS = 30


hero = Actor("hero", (50, 50))
hero.health = 130
hero.attack = 7


bg = Actor("lanetli_orman", (WIDTH // 2, HEIGHT // 2))
win = Actor("win")
gameover = Actor("gameover")
level = 1

wolfs = []
soldiers = []
giants = []
bosses = []


def create_wolfs():
    wolfs.clear()
    for i in range(random.randint(2, 5)):
        wolf = Actor("kurt", (random.randint(200, 800), random.randint(200, 800)))
        wolf.health = random.randint(5,10)
        wolf.attack = random.randint(5, 8)
        wolfs.append(wolf)


def create_soldiers():
    soldiers.clear()
    for i in range(random.randint(3, 5)):
        soldier = Actor("asker", (random.randint(200, 800), random.randint(200, 800)))
        soldier.health = random.randint(15,25)
        soldier.attack = random.randint(8, 12)
        soldiers.append(soldier)


def create_giants():
    giants.clear()
    for i in range(2):
        giant = Actor("zincirli_dev", (random.randint(300, 700), random.randint(300, 700)))
        giant.health = 60
        giant.attack = 12
        giants.append(giant)


def create_boss():
    bosses.clear()
    boss = Actor("final_boss", (WIDTH // 2, HEIGHT // 2))
    boss.health = 180
    boss.attack = 18
    bosses.append(boss)

create_wolfs()


def on_key_down(key):
    if key == keys.LEFT and hero.x > 50:
        hero.x -= 25
    if key == keys.RIGHT and hero.x < 950:
        hero.x += 25
    if key == keys.UP and hero.y > 50:
        hero.y -= 25
    if key == keys.DOWN and hero.y < 950:
        hero.y += 25


def update():
    global level

    
    if level == 1:
        i = hero.collidelist(wolfs)
        if i != -1:
            wolf = wolfs[i]
            wolf.health -= hero.attack
            hero.health -= wolf.attack
            if wolf.health <= 0:
                wolfs.pop(i)

        if not wolfs:
            level = 2
            hero.health += 50      
            hero.attack += 3      
            hero.pos = (50, 50)
            bg.image = "kizil_bataklik"
            create_soldiers()

    
    elif level == 2:
        i = hero.collidelist(soldiers)
        if i != -1:
            soldier = soldiers[i]
            soldier.health -= hero.attack
            hero.health -= soldier.attack
            if soldier.health <= 0:
                soldiers.pop(i)

        if not soldiers:
            level = 3
            hero.health += 50
            hero.attack += 3
            hero.pos = (50, 50)
            bg.image = "kayip_harabeler"
            create_giants()

   
    elif level == 3:
        i = hero.collidelist(giants)
        if i != -1:
            giant = giants[i]
            giant.health -= hero.attack
            hero.health -= giant.attack
            if giant.health <= 0:
                giants.pop(i)

        if not giants:
            level = 4
            hero.health += 50
            hero.attack += 3
            hero.pos = (50, 50)
            bg.image = "taht_odasi"
            create_boss()

    
    elif level == 4:
        i = hero.collidelist(bosses)
        if i != -1:
            boss = bosses[i]
            boss.health -= hero.attack
            hero.health -= boss.attack
            if boss.health <= 0:
                bosses.pop(i)
                level = 5

def draw():
    bg.draw()
    hero.draw()

    if level == 1:
        for w in wolfs:
            w.draw()
    elif level == 2:
        for s in soldiers:
            s.draw()
    elif level == 3:
        for g in giants:
            g.draw()
    elif level == 4:
        for b in bosses:
            b.draw()
    elif level == 4 and  hero.health<0:
        gameover.draw()
    elif level == 5 and hero.health>0:
        win.draw()
    elif level ==5 and hero.health<0:
        gameover.draw()

        

    screen.draw.text(f"CAN: {hero.health}", (20, 20), color="white", fontsize=36)
    screen.draw.text(f"SALDIRI: {hero.attack}", (20, 60), color="white", fontsize=36)
    screen.draw.text(f"SEVİYE: {level}", (20, 100), color="white", fontsize=36)

pgzrun.go()


