from ctypes import py_object
import pygame
import random
import os
pygame.mixer.init()
pygame.init()

#colors
white=(255,255,255)
red=(255,0,0)
black=(0,0,0)

#Screen width and hight
screen_width=900
screen_height=600
#Creating Window
game_window=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("My Own Snake_Game")
pygame.display.update()
# Make Clock To set Frames per Second
clock = pygame.time.Clock()
#Variables to set snake's x and y direction or valocity or to make snake head
font=pygame.font.SysFont(None,55)

#Back-Groung Images
#For Game Over
bg_img=pygame.image.load("snake.jpg")
bg_img=pygame.transform.scale(bg_img,(screen_width,screen_height)).convert_alpha()
#For Home Page
bg_img1=pygame.image.load("snake2.jpg")
bg_img1=pygame.transform.scale(bg_img1,(screen_width,screen_height)).convert_alpha()

# To set "Screen" text on game_window
def text_screen(text,color,x,y):
    screen_text=font.render(text,True,color)
    game_window.blit(screen_text,[x,y])

#this function make snake head and increase the size
def plot_snake(game_window,color,snk_list,snake_size):
    for x,y in snk_list:
        pygame.draw.rect(game_window, color, [x, y, snake_size, snake_size])

#Function For WelCome Page
def welcome():
    exit_game=False
    while not exit_game:
        game_window.fill(white)
        game_window.blit(bg_img1,(0,0))

        text_screen("WelCome To Snake Game", (0,0,255), 180, 80)
        text_screen("Press Space To Start This Game!!",(0,0,255), 150, 120)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit_game=True
            #When You press Space button then game will start
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    gameloop()
        pygame.display.update()
        clock.tick(60)

#To hold the window and to controll all events  OR "GAME LOOP FUNCTION"
def gameloop():
    # Required Variables for gameloop
    snake_x = 50
    snake_y = 50
    snake_size = 15
    velocity_x = 0
    velocity_y = 0
    init_velocity = 5
    food_x = random.randint(20, screen_width / 2)
    food_y = random.randint(20, screen_height / 2)
    # variable for score
    score = 0
    #frame per second
    fps = 30

    # Event Required Variables
    game_over = False
    exit_game = False

    # TO increase the size of snake
    snk_length = 1
    snk_list = []
    #If you Highscore.txt file is deleted then to set this Buggs we can use following condition
    if not os.path.exists("HighScore.txt"):
        with open("HighScore.txt","w") as f:
            f.write("0")
    #To Read High_Score From the file
    with open("HighScore.txt","r") as f:
        highscore=f.read()

    while not exit_game:
        #This condition will execute when game_over is True
        if game_over:
            #TO Store the High Score in the file
            with open("HighScore.txt", "w") as f:
                f.write(str(highscore))

            game_window.fill(white)
            game_window.blit(bg_img, (0, 0))
            text_screen("Game Over! Press Enter TO Continue",red,100,450)

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    exit_game = True

                #When you pressed Enter
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        welcome()


        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = - init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = - init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x)<8 and abs(snake_y - food_y)<8:
                score +=10
                food_x = random.randint(20, screen_width / 2)
                food_y = random.randint(20, screen_height / 2)
                snk_length +=5
                pygame.mixer.music.load("snakehiss.mp3")
                pygame.mixer.music.play()
                #To Print High_Score to the Screen
                if score > int(highscore): #From the file highscore is of str type
                    highscore=score


            game_window.fill(white)
            text_screen("Score: " + str(score) + "   HighScore:"+str(highscore), red, 5, 5)
            pygame.draw.rect(game_window, red, [food_x, food_y, snake_size, snake_size])


            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]
             #When snake Touch itself then this condition will run, Here snk_list[:-1] ->Means In snk_list last element(Head) is excluded
            if head in snk_list[:-1]:
                game_over=True
                pygame.mixer.music.load("snakehit.mp3")
                pygame.mixer.music.play()

            #Make Condition for Collision of snake to the wall
            if (snake_x<0 or snake_x>screen_width) or (snake_y<0 or snake_y>screen_height):
                game_over=True
                pygame.mixer.music.load("snakehit.mp3")
                pygame.mixer.music.play()


            # pygame.draw.rect(gameWindow, black, [snake_x, snake_y, snake_size, snake_size])
            plot_snake(game_window, black, snk_list, snake_size)
        #END OF ELSE BLOCK

        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()

welcome()




