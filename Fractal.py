import turtle
import random
import os
import time
import pygame
import sys
import math
import random
import time
pygame.init()
info = pygame.display.Info()
screen_width = info.current_w
screen_height = info.current_h
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
background_color = (0, 0, 0) 
clock = pygame.time.Clock()
white = (255, 255, 255)
green = (0, 255, 0)
darker_green = (0, 200, 0)
blue = (0, 0, 128)
black = (0, 0, 0)
greyish = (170, 170, 170)
light_blue = (0, 200, 250)
red = (200, 0, 0)
turtle.speed(0)
turtle.hideturtle()
turtle.bgcolor("black")
turtle.pencolor("white")
screen2 = turtle.Screen()
screen2.title("Fragile Soul")
file_names = ["currency", "level", "era", "upgrade_1", "upgrade_2", "orbs"]
switch1 = True
switch2 = True
switch3 = True

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def save(file):
    x = globals()[file]
    if file != "orbs":
        with open((file) + ".txt", "w") as file:
            file.write(str(x))
    else:
        with open("orbs.txt", "w") as file:
            for line in orbs:
                file.write(str(f"{line}\n"))


def wipe_files():
    for file in file_names:
        if file != "orbs":
            with open((file) + ".txt", "w") as file:
                file.write(str(0))
        else:
            num = 0
            with open((file) + ".txt", "w") as file:
                values = []
                for i in range(3):
                    values.append(0)
                for line in values:
                    file.write(f"{str(line)}\n")
    main()

def triangle(signal1, signal2, signal3):
    screen2.tracer(0) 
    turtle.clear()
    for i in range(level):
        color = 1
        turtle.penup()
        turtle.forward(10 + level)
        turtle.pendown()
        turtle.left(10 + (era + 7.5))
        for i in range(3):
            turtle.penup()
            if color == 1:
                turtle.pencolor("blue")
            elif color == 2:
                turtle.pencolor("green")
            elif color == 3:
                turtle.pencolor("red")
            if signal1 == True and color == 1:
                turtle.pendown()
            if signal2 == True and color == 2:
                turtle.pendown()
            if signal3 == True and color == 3:
                turtle.pendown()
            turtle.forward(120-(10 + level))
            turtle.left(120)
            if color == 3:
                color = 0
            color +=1
        turtle.penup()
        screen2.update()

def load_files():
    global currency, level, era, upgrade_1, upgrade_2, orbs
    orbs = []
    Loaded = False
    while Loaded == False:
        try:
            with open("currency.txt", "r") as file:
                currency = int(file.read())
            with open("level.txt", "r") as file:
                level = int(file.read())
            with open("era.txt", "r") as file:
                era = int(file.read())
            with open("upgrade_1.txt", "r") as file:
                upgrade_1 = int(file.read())
            with open("upgrade_2.txt", "r") as file:
                upgrade_2 = int(file.read())
            with open("orbs.txt", "r") as file:
                pre_orbs = (file.readlines())
                for line in pre_orbs:
                    orbs.append(int(line))
            Loaded = True
        except:
            wipe_files()


def pytext(text, x, y, font_size, color1, color2):
    font = pygame.font.Font('freesansbold.ttf', font_size)
    text = font.render(text, True, color1, color2)
    textRect = text.get_rect()
    textRect.center = (x, y)
    screen.blit(text, textRect)

def call_orb(orb_level, orby):
    orb_store = [
        {"subfont": 16, "font": 22, "subText": "Doubles Speed", "Text": "Doubles Speed", "color": light_blue, "action#": 1, "level": 1, "orb_num": 1, "int": 1, "cost": 5000, "cost_font": 18},
        {"subfont": 16, "font": 22, "subText": "In Progress", "Text": "In progress", "color": green, "action#": 2, "level": 2, "orb_num": 2, "int": 1, "cost": 50000, "cost_font": 18}
    ]
    orb_rect = []
    for orb in orb_store:
        if orb_level >= orb["level"] and orbs[orb["orb_num"]-1] < orb["int"]:
            orb_rect.append(orb_store[orb["action#"] - 1])
        elif orbs[orb["orb_num"] - 1] >= orb["int"]:
            try:
                orb_rect.remove(orb_store[orb["action#"] - 1])
            except:
                filler = 0
    orby = 0
    use_orb = []
    for item in orb_rect:
        pygame.draw.rect(screen, item["color"], pygame.Rect(1000, 100 + orby, 200, 100))
        pytext(item["Text"], 1100, 125 + orby, item["font"], black, item["color"])
        pytext(item["subText"], 1100, 150 + orby, item["subfont"], black, item["color"])
        pytext(f"Costs: {item["cost"]}", 1100, 170 + orby, item["cost_font"], black, item["color"])
        use_orb.append({"rect": pygame.Rect(1000, 100 + orby, 200, 100), "color": item["color"], "action": f"rect{item["action#"]}_clicked", "cost": item["cost"]})
        orby += 120
    return use_orb
    
def start_new_era():
    global currency, level, era, upgrade_1, upgrade_2, orbs
    era += 1
    level = 1
    turtle.up()
    turtle.goto(0, 0)
    for file in file_names:
        if file != "era" and file != orbs:
            with open((file) + ".txt", "w") as file:
                file.write(str(0))
        elif file == orbs:
            with open((file) + ".txt", "w") as file:
                values = []
                for i in range(3):
                    values.append(0)
                for line in values:
                    file.write(f"{str(line)}\n")

def main():
    global currency, level, era, upgrade_1, upgrade_2, orbs
    load_files()
    pygame.display.set_caption(f"Incremental")
    if level < 1:
        level = 1
        save("level")
    running = True
    start = True
    update_time = 0
    darker1 = 1
    darker2 = 1
    darker3 = 1
    dark1 = False
    dark2 = False
    dark3 = False
    switch1 = True
    switch2 = True
    switch3 = True
    triangle(switch1, switch2, switch3)
    if era < 1:
        era = 1
        save("era")
    clear_console()
    menu = True
    confirmation = False
    while running:
        while menu == True:
            confirmation_rect = [
                {"rect": pygame.Rect(800, 500, 400, 300), "color": greyish, "action": "rect1_clicked"},
                {"rect": pygame.Rect(950, 600, 50, 200), "color": darker_green, "action": "rect2_clicked"}
            ]
            menu_rect = [
                {"rect": pygame.Rect(300, 100, 200, 100), "color": darker_green, "action": "rect1_clicked"},
                {"rect": pygame.Rect(520, 100, 200, 100), "color": red, "action": "rect2_clicked"}
            ]
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    for item in menu_rect:
                        if item["rect"].collidepoint(mouse_pos):
                            if item["action"] == "rect1_clicked":
                                menu = False
                            if item["action"] == "rect2_clicked":
                                confirmation = True
                    for item in confirmation_rect:
                        if item["rect"].collidepoint(mouse_pos):
                            if item["action"] == "rect2_clicked":
                                wipe_files()
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            screen.fill(background_color)
            for item in menu_rect:
                pygame.draw.rect(screen, item["color"], item["rect"])
            pytext(f"Wipe Save", 620, 145, 20, black, red)
            pytext(f"Start", 400, 145, 25, black, darker_green)
            if confirmation == True:
                for item in confirmation_rect:
                    pygame.draw.rect(screen, item["color"], item["rect"])
            pygame.display.flip()
        load_files()
        level_scale = (10)**level
        TcT = 1000/(orbs[0]+1)
        new_era = (era*240)/(era+1)
        boost2 = upgrade_2
        boost1 = (upgrade_1) * (boost2 + 1)
        upgrade_rect = [
            {"rect": pygame.Rect(300, 100, 200, 100), "color": (170, 170, 170), "action": "rect1_clicked"},
            {"rect": pygame.Rect(520, 100, 200, 100), "color": (170, 170, 170), "action": "rect2_clicked"}
        ]
        switch_rect = [
            {"rect": pygame.Rect(100, 400, 50, 50), "color": (0, 0, 255 * darker1), "action": "rect1_clicked"},
            {"rect": pygame.Rect(100, 500, 50, 50), "color": (0, 255 * darker2, 0), "action": "rect2_clicked"},
            {"rect": pygame.Rect(100, 600, 50, 50), "color": (255 * darker3, 0, 0), "action": "rect3_clicked"}
        ]
        cost1 = (round((upgrade_1 * ((10 + upgrade_1)**1.25))))
        cost2 = (round((upgrade_2 + 1)**(2.5+((upgrade_2 + 2)/2)))) + 100
        if start == True:
            for rectangle in upgrade_rect:
                pygame.draw.rect(screen, rectangle["color"], rectangle["rect"])
            start = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    menu = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for item in upgrade_rect:
                    if item["rect"].collidepoint(mouse_pos):
                        if item["action"] == "rect1_clicked":
                            if currency >= cost1:
                                upgrade_1 += 1
                                currency -= cost1
                                save("upgrade_1")
                                save("currency")
                        if level >= 3:
                            if item["action"] == "rect2_clicked":
                                if currency >= cost2:
                                    upgrade_2 += 1
                                    currency -= cost2
                                    save("upgrade_2")
                                    save("currency")
                for item in switch_rect:
                    if item["rect"].collidepoint(mouse_pos):
                        if item["action"] == "rect1_clicked" and dark1 == False:
                            darker1 = 1/2
                            dark1 = True
                            switch1 = False
                        elif item["action"] == "rect1_clicked" and dark1 == True:
                            darker1 = 1
                            dark1 = False
                            switch1 = True
                        if item["action"] == "rect2_clicked" and dark2 == False:
                            darker2 = 1/2
                            dark2 = True
                            switch2 = False
                        elif item["action"] == "rect2_clicked" and dark2 == True:
                            darker2 = 1
                            dark2 = False
                            switch2 = True
                        if item["action"] == "rect3_clicked" and dark3 == False:
                            darker3 = 1/2
                            dark3 = True
                            switch3 = False
                        elif item["action"] == "rect3_clicked" and dark3 == True:
                            darker3 = 1
                            dark3 = False
                            switch3 = True
                        triangle(switch1, switch2, switch3)
                for item in orb_rect:
                    if item["rect"].collidepoint(mouse_pos):
                        if item ["action"] == "rect1_clicked" and currency >= item["cost"]:
                            if orbs[0] != 1:
                                currency -= item["cost"]
                                orbs[0] = 1
                                save("orbs")
                                save("currency")

        current_time = pygame.time.get_ticks()

        if current_time - update_time > TcT:
            update_time = current_time
            currency += ((1 + boost1) * level)**era
            save("currency")
        
        if currency >= level_scale:
            level += 1
            triangle(switch1, switch2, switch3)
            save("level")
            save("currency")
        
        if level >= new_era:
            start_new_era()

        screen.fill(background_color)
        orb_level = 0
        if level >= 2:
            pygame.draw.rect(screen, upgrade_rect[0]["color"], upgrade_rect[0]["rect"])
            pytext(f"Soul Strength: {upgrade_1}", 400, 120, (22-round(upgrade_1**0.01)), black, greyish)
            pytext(f"Energy per second:", 400, 145, 15, black, greyish)
            pytext(f"+ {(boost2 + 1) * level} per level (+{(boost1 + 1) * level})", 400, 165, (15-round(boost1**0.01)), black, greyish)
            pytext(f"Cost: {cost1}", 400, 190, 15, black, greyish)
        if level >= 3:
            pygame.draw.rect(screen, upgrade_rect[1]["color"], upgrade_rect[1]["rect"])
            pytext(f"Soul Aura: {upgrade_2}", 620, 120, (22-round(upgrade_2**0.01)), black, greyish)
            pytext(f"Strength Base:", 620, 145, 15, black, greyish)
            pytext(f"+1 per level: (+{boost2})", 620, 165, (15-round(boost2**0.01)), black, greyish)
            pytext(f"Cost: {cost2}", 620, 190, 15, black, greyish)
            orb_level = 1
        if level >= 5:
            orb_level = 2
        
        #------
        pytext(f"Energy: {currency}", 150, 100, (28-round(currency**0.01)), white, black)
        pytext(f"(Energy Per Sec: {((1 + boost1) * level)**era})", 150, 125, 16, white, black)
        pytext(f"Soul Level: {level}", 150, 150, 28, white, black)
        pytext(f"Soul Era: {era}", 150, 200, 28, white, black)
        pytext(f"(Next Level at: {level_scale} Energy)", 150, 175, 16, white, black)
        pytext(f"Soul Switches:", 125, 380, 15, white, black)
        for item in switch_rect:
            pygame.draw.rect(screen, item["color"], item["rect"])
        orby = 0
        orb_rect = call_orb(orb_level, orby)
        pygame.display.flip()
        clock.tick(60)
main()
#wipe_files()