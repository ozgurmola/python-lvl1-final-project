import pgzrun
import random

TITLE = "ARİNİN MACERALARI"
WIDTH = 1000
HEIGHT = 1000
FPS = 30


mode = "start"   
level = 1


hero = Actor("hero", (50, 50))
hero.health = 130
hero.attack = 7

bg = Actor("lanetli_orman", (WIDTH//2, HEIGHT//2))
menu = Actor("giriş", (WIDTH//2, HEIGHT//2))
win_screen = Actor("win", (WIDTH//2, HEIGHT//2))
gameover = Actor("gameover", (WIDTH//2, HEIGHT//2))

wolfs = []
soldiers = []
giants = []
bosses = []


def create_wolfs():
    wolfs.clear()
    for _ in range(random.randint(2, 5)):
        w = Actor("kurt", (random.randint(200,800), random.randint(200,800)))
        w.health = random.randint(5,10)
        w.attack = random.randint(5,8)
        wolfs.append(w)

def create_soldiers():
    soldiers.clear()
    for _ in range(random.randint(3,5)):
        s = Actor("asker", (random.randint(200,800), random.randint(200,800)))
        s.health = random.randint(15,25)
        s.attack = random.randint(8,12)
        soldiers.append(s)

def create_giants():
    giants.clear()
    for _ in range(2):
        g = Actor("zincirli_dev", (random.randint(300,700), random.randint(300,700)))
        g.health = 40
        g.attack = 12
        giants.append(g)

def create_boss():
    bosses.clear()
    b = Actor("final_boss", (WIDTH//2, HEIGHT//2))
    b.health = 80
    b.attack = 15
    bosses.append(b)


def reset_game():
    global level, mode
    level = 1
    mode = "game"
    hero.pos = (50,50)
    hero.health = 130
    hero.attack = 7
    bg.image = "lanetli_orman"
    create_wolfs()


def on_key_down(key):
    global mode

    if mode == "start" and key == keys.SPACE:
        reset_game()

    if mode in ("win", "end") and key == keys.SPACE:
        mode = "start"

    if mode != "game":
        return

    if key == keys.LEFT and hero.x > 50:
        hero.x -= 25
    if key == keys.RIGHT and hero.x < 950:
        hero.x += 25
    if key == keys.UP and hero.y > 50:
        hero.y -= 25
    if key == keys.DOWN and hero.y < 950:
        hero.y += 25


def update():
    global level, mode

    if mode != "game":
        return

    if hero.health <= 0:
        mode = "end"

    if level == 1:
        i = hero.collidelist(wolfs)
        if i != -1:
            wolfs[i].health -= hero.attack
            hero.health -= wolfs[i].attack
            if wolfs[i].health <= 0:
                wolfs.pop(i)

        if not wolfs:
            level = 2
            hero.pos=(50,50)
            hero.health += 50
            hero.attack += 3
            bg.image = "kizil_bataklik"
            create_soldiers()

    elif level == 2:
        i = hero.collidelist(soldiers)
        if i != -1:
            soldiers[i].health -= hero.attack
            hero.health -= soldiers[i].attack
            if soldiers[i].health <= 0:
                soldiers.pop(i)

        if not soldiers:
            level = 3
            hero.pos=(50,50)
            hero.health += 50
            hero.attack += 3
            bg.image = "kayip_harabeler"
            create_giants()

    elif level == 3:
        i = hero.collidelist(giants)
        if i != -1:
            giants[i].health -= hero.attack
            hero.health -= giants[i].attack
            if giants[i].health <= 0:
                giants.pop(i)

        if not giants:
            level = 4
            hero.pos=(50,50)
            hero.health += 50
            hero.attack += 3
            bg.image = "taht_odasi"
            create_boss()

    elif level == 4:
        i = hero.collidelist(bosses)
        if i != -1:
            bosses[i].health -= hero.attack
            hero.health -= bosses[i].attack
            if bosses[i].health <= 0:
                bosses.pop(i)
                mode = "win"

def draw():
    if mode == "start":
        menu.draw()
        return

    if mode == "win":
        win_screen.draw()
        return

    if mode == "end":
        gameover.draw()
        return

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



    screen.draw.text(f"CAN: {hero.health}", (20,20), color="white", fontsize=36)
    screen.draw.text(f"SALDIRI: {hero.attack}", (20,60), color="white", fontsize=36)
    screen.draw.text(f"SEVİYE: {level}", (20,100), color="white", fontsize=36)

pgzrun.go()




