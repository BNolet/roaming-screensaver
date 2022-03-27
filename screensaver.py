import pygame
import random
clock = pygame.time.Clock()

pygame.init()
pygame.display.set_caption("Kinda red")
width = 1305
height = 745
screen = pygame.display.set_mode((width,height))
logo = pygame.image.load('dvd.png').convert_alpha()
logo_resized = pygame.transform.scale(logo, (logo.get_width()*0.35,logo.get_height()*0.35))
x = 5
y = 5
right = True
down = True

def fills_init():
    purple = (106, 84, 149)
    pink = (237, 94, 221)
    green = (139, 219, 129)
    blue = (84, 140, 255)
    global fills
    fills = list(locals().values())
    global current_fill
    current_fill = fills[0]

def fill_screen(screen, current_fill, border_colour, border=10):
    screen.fill(border_colour)
    screen.fill(current_fill, screen.get_rect().inflate(-border, -border))



fills_init()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    fill_screen(screen,current_fill,(0,0,0),10)
    if right == True:
        x = x + 3
    else:
        x = x - 3

    if down == True:
        y = y + 3
    else:
        y = y - 3
    
    if x >= width-logo_resized.get_width()-5 or x <= 5:
        right = not right
        current_fill = random.choice([colour for colour in fills if colour is not current_fill])

    if y >= height-logo_resized.get_height()-5 or y <= 5:
        down = not down
        current_fill = random.choice([colour for colour in fills if colour is not current_fill])

    screen.blit(logo_resized, (x,y))
    pygame.display.flip()
    clock.tick(30)