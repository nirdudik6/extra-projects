from tkinter import *
from selenium import webdriver
from time import sleep
import pygame
import random
import sys
import pywhatkit



print("hello welcome to my project!")
while (True):
    route=input("enter your choise: (choose 1-4)\n1.game\n2.send message on whatsapp\n3.stats of messages that i sent\n4.login to instagram\n")
    if route=="1":
        pygame.init()
        WIDTH = 1920
        HEIGHT = 1080
        RED = (255, 0, 0)
        BLUE = (0, 0, 255)
        YELLOW = (255, 255, 0)
        BACKGROUND_COLOR = (0, 0, 0)
        player_size = 50
        player_pos = [WIDTH / 2, HEIGHT - 2 * player_size]
        enemy_size = 50


        enemy_pos = [random.randint(0, WIDTH - enemy_size), 0]
        enemy_list = [enemy_pos]
        SPEED = 10
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        game_over = False
        score = 0
        clock = pygame.time.Clock()
        myFont = pygame.font.SysFont("monospace", 35)
        def close_window():
            window.destroy()
            print("GAME OVER!\nYou've got " + str(score) + " points!")
            exit()
        def set_level(score, SPEED):
            if score < 20:
                SPEED = 5
            elif score < 40:
                SPEED = 8
            elif score < 60:
                SPEED = 12
            elif score < 80:
                SPEED = 15
            elif score < 120:
                SPEED = 18
            elif score < 180:
                SPEED = 22
            else:
                SPEED = 27
            return SPEED

        def drop_enemies(enemy_list):
            delay = random.random()
            if len(enemy_list) < 10 and delay < 0.1:
                x_pos = random.randint(0, WIDTH - enemy_size)
                y_pos = 0
                enemy_list.append([x_pos, y_pos])

        def draw_enemies(enemy_list):
            for enemy_pos in enemy_list:
                pygame.draw.rect(screen, BLUE, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))

        def update_enemy_positions(enemy_list, score):
            for idx, enemy_pos in enumerate(enemy_list):
                if enemy_pos[1] >= 0 and enemy_pos[1] < HEIGHT:
                    enemy_pos[1] += SPEED
                else:
                    enemy_list.pop(idx)
                    score += 1
            return score

        def collision_check(enemy_list, player_pos):
            for enemy_pos in enemy_list:
                if detect_collision(enemy_pos, player_pos):
                    return True
            return False

        def detect_collision(player_pos, enemy_pos):
            p_x = player_pos[0]
            p_y = player_pos[1]
            e_x = enemy_pos[0]
            e_y = enemy_pos[1]
            if (e_x >= p_x and e_x < (p_x + player_size)) or (p_x >= e_x and p_x < (e_x + enemy_size)):
                if (e_y >= p_y and e_y < (p_y + player_size)) or (p_y >= e_y and p_y < (e_y + enemy_size)):
                    return True
            return False

        while not game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    x = player_pos[0]
                    y = player_pos[1]
                    if event.key == pygame.K_LEFT:
                        x -= player_size
                    elif event.key == pygame.K_RIGHT:
                        x += player_size
                    player_pos = [x, y]
            screen.fill(BACKGROUND_COLOR)
            drop_enemies(enemy_list)
            score = update_enemy_positions(enemy_list, score)
            SPEED = set_level(score, SPEED)
            text = "Score:" + str(score)
            label = myFont.render(text, 1, YELLOW)
            screen.blit(label, (WIDTH - 200, HEIGHT - 40))
            if collision_check(enemy_list, player_pos):
                game_over = True
                break
            draw_enemies(enemy_list)
            pygame.draw.rect(screen, RED, (player_pos[0], player_pos[1], player_size, player_size))
            clock.tick(30)
            pygame.display.update()
        if game_over:
            window = Tk()
            window.geometry("1400x700")
            window.title("GAME OVER!")
            window.configure(background="black")
            Label(window, text="\n\n\n\n\n\nGAME OVER!\nYou've got " + str(score) + " points!", width=60, bg="black",fg="red", font="verdana 30 italic").grid(row=1, column=0, sticky='W')
            Label(window, text="exit and try again!", width=60, bg="black", fg="red", font="verdana 30 italic").grid(row=7, column=0, sticky='W')
            Button(window, text="EXIT", width=14, command=close_window, font="none 12 italic").grid(row=13, column=0,sticky=S)
            window.mainloop()

    elif route=="2":
        print("let's send a message!")
        print("I need some details:\n")
        phone=input("enter the phone number:\n")
        msg=input("enter your message:\n")
        hour=int(input("enter the hour of sending:\n"))
        min=int(input("enter the minutes of sending:\n"))
        pywhatkit.sendwhatmsg( phone, msg, hour, min)
        print("sent!")
        continue

    elif route == "3":
        while (True):
            opt=input("Enter your choise:\n1.show the messages that sent\n2.delete the list of messages that sent\n")
            if opt=="1":
                print("Here's the messages that sent so far:\n")
                path=r"C:/Users/yoval/PycharmProjects/pythonProject1/nir's projects/pywhatkit_dbs.txt"
                file=open(path, "r")
                print(file.read())
                break
            elif opt=="2":
                path = r"C:/Users/yoval/PycharmProjects/pythonProject1/nir's projects/pywhatkit_dbs.txt"
                file = open(path, "w")
                print("done!")
                break
            else:
                print("incorrect number!")
                continue

    elif route=="4":
        class Instalogin:
            def __init__(self, username, password):
                self.driver = webdriver.Chrome('C:/Users/yoval/Desktop/chromedriver')
                self.driver.get("https://instagram.com")
                sleep(2)
                username_type = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")
                username_type.send_keys(username)
                password_type = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")
                password_type.send_keys(password)
                sleep(2)
                submit = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button')
                submit.click()


        print("Let's connect to instagram!")
        username=input("enter your username:\n")
        password=input("enter your password:\n")
        my_bot = Instalogin(username, password)
        my_bot.Instalogin()
        print("done!")
        try:
            my_bot.driver.close()
        except:
            print("Fail")
            my_bot.driver.close()

    else:
        print("incorrect number!")
        continue
    if (input("do you want to exit? y/n\n") == "y"):
        break
    print("thanks and bye bye...")





