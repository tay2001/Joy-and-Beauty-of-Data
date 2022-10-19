#pygame development 1
#Start the basic game set up
#Set up the display

#-------------------------------------#
import pygame

pygame.init()

#screen size
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = 'Crossy RPG'

#color codes with RGB
WHITE_COLOR = (255,255,255)
BLACK_COLOR = (0,0,0)

#set FPS - 60 base
clock = pygame.time.Clock()
TICK_RATE = 60

#check if game is over for the loop
is_game_over = False

#Create the window of specified size in white to display the game
game_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
#Set the game window color to white
game_screen.fill(WHITE_COLOR)
pygame.display.set_caption(SCREEN_TITLE)

player_image = pygame.image.load('')


#run game if over is false
#runs until is_game_over = true
while not is_game_over:

    #a loop to get all of the events occuring at any given time
    #events are most often mouse movement, mouse and button clicks, or exit events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_game_over = True

        print(event)

    pygame.draw.rect(game_screen, BLACK_COLOR, [350,350,100,100])
    pygame.draw.circle(game_screen, BLACK_COLOR, (400,300),50)

    #update all the game graphics
    pygame.display.update()
    #tick the clock to update everything within the game
    clock.tick(TICK_RATE)

    #quit pygame and the program
pygame.quit()
quit()
    



