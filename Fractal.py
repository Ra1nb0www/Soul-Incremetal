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
blue = (0, 0, 128)
black = (0, 0, 0)
greyish = (170, 170, 170)
turtle.speed(0)
turtle.hideturtle()
turtle.bgcolor("black")
turtle.pencolor("white")
screen2 = turtle.Screen()
screen2.title("Fragile Soul")
file_names = ["currency", "level", "era", "upgrade_1"]

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def save(file):
    x = globals()[file]
    with open((file) + ".txt", "w") as file:
        file.write(str(x))

def wipe_files():
    for file in file_names:
        with open((file) + ".txt", "w") as file:
            file.write(str(0))

def triangle():
    turtle.forward(10 + level)
    turtle.left(10 + (era * 5))
    for i in range(3):
        turtle.pendown()
        turtle.forward(120-(10 + level))
        turtle.left(120)
    turtle.penup()

def load_files():
    global currency, level, era, upgrade_1
    try:
        with open("currency.txt", "r") as file:
            currency = int(file.read())
        with open("level.txt", "r") as file:
            level = int(file.read())
        with open("era.txt", "r") as file:
            era = int(file.read())
        with open("upgrade_1.txt", "r") as file:
            upgrade_1 = int(file.read())
    except:
        wipe_files()
    finally:
        with open("currency.txt", "r") as file:
            currency = int(file.read())
        with open("level.txt", "r") as file:
            level = int(file.read())
        with open("era.txt", "r") as file:
            era = int(file.read())
        with open("upgrade_1.txt", "r") as file:
            upgrade_1 = int(file.read())

def pytext(text, x, y, font_size, color1, color2):
    font = pygame.font.Font('freesansbold.ttf', font_size)
    text = font.render(text, True, color1, color2)
    textRect = text.get_rect()
    textRect.center = (x, y)
    screen.blit(text, textRect)

def main():
    global currency, level, era, upgrade_1
    load_files()
    pygame.display.set_caption(f"Incremental")
    if level < 1:
        level = 1
        save("level")
    running = True
    start = True
    update_time = 0
    for i in range(level):
        triangle()
    if era < 0:
        era = 1
        save("era")
    clear_console()
    while running:
        load_files()
        TcT = 1000
        new_era = (75)**era
        upgrade_1_rect = [
            {"rect": pygame.Rect(300, 100, 200, 100), "color": (170, 170, 170), "action": "rect1_clicked"}
        ]
        if start == True:
            for rectangle in upgrade_1_rect:
                pygame.draw.rect(screen, rectangle["color"], rectangle["rect"])
            start = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for item in upgrade_1_rect:
                    if item["rect"].collidepoint(mouse_pos):
                        if item["action"] == "rect1_clicked":
                            if currency >= (round((currency)+currency*0.75)):
                                upgrade_1 += 1
                                currency -= (round((currency)+currency*0.75))
                                save("upgrade_1")
                                save("currency")
        current_time = pygame.time.get_ticks()

        if current_time - update_time > TcT:
            update_time = current_time
            currency += ((1 + upgrade_1) * level)**era
            save("currency")
        
        if currency >= (25)**(int(round(level)/2)):
            turtle.clear()
            level += 1
            for i in range(level):
                triangle()
            save("level")
            save("currency")
        
        if level >= new_era:
            era += 1
            level = 1
            turtle.clear()
            turtle.up()
            turtle.goto(0, 0)
            save("level")
            save("era")
        screen.fill(background_color)
        for rectangle in upgrade_1_rect:
            pygame.draw.rect(screen, rectangle["color"], rectangle["rect"])
        pytext(f"Soul Strength: {upgrade_1}", 400, 125, (22-round(upgrade_1**0.1)), black, greyish)
        pytext(f"Energy per second:", 400, 150, 15, black, greyish)
        pytext(f"+ 1 per level", 400, 175, 15, black, greyish)
        #------
        pytext(f"Energy: {currency}", 150, 100, (28-round(currency**0.1)), white, black)
        pytext(f"Soul Level: {level}", 150, 150, 28, white, black)
        pytext(f"Soul Era: {era}", 150, 200, 28, white, black)
        pygame.display.flip()
        clock.tick(60)
main()
#wipe_files()