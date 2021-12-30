import pygame
from pygame.constants import *

pygame.init()
clock = pygame.time.Clock()
clock.tick(60)
screen_size = (470, 620)
screen = pygame.display.set_mode(screen_size)
font = pygame.font.Font(None, 32)

running = True

hill = [
    ('#             @'),
    ('               '),
    ('               '),
    (' @  #          '),
    ('               '),
    ('               '),
    ('       @    @  '),
    ('               '),
    ('               '),
    ('     @    @    '),
    ('               '),
    ('               '),
    (' @  #          '),
    ('               '),
    ('               '),
    ('       @    @  '),
    ('               '),
    ('               '),
    ('     @    @    '),
    ('               '),]


def update_fps():
    fps = str(int(clock.get_fps()))
    fps_text = font.render(fps, 1, pygame.Color("coral"))
    return fps_text

y_speed = 0.25
x_speed = 0.25
offset = 0
bg = pygame.image.load('images/bg.jpeg').convert()
rock = pygame.transform.scale(pygame.image.load('images/rock.png'), (30, 30)).convert_alpha()
snowman = pygame.transform.scale(pygame.image.load('images/snowman.png'), (30, 30)).convert_alpha()
ski_right = pygame.transform.scale(pygame.image.load('images/ski_right.png'), (30, 30)).convert_alpha()
ski_left = pygame.transform.scale(pygame.image.load('images/ski_left.png'), (30, 30)).convert_alpha()


screen.blit(bg, (0, 0))

first = True
skier_direction = 'right'
skier_location = 235

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_h:
                skier_direction = 'left'
            elif event.key == K_j:
                skier_direction = 'right'

    # screen.blit(bg, (0, 0))

    # erase skier
    old_skier_rect = (skier_location, 10, 30, 30)

    for y, row in enumerate(hill):
        for x, item in enumerate(row):
            old_rect = pygame.Rect((int(10 + x * 30), int(10 + y * 30 - offset + y_speed), 30, 30))
            if first:
                first = False
            else:
                # erase old locations
                screen.blit(bg, old_rect, old_rect)

            new_location = pygame.Rect((10 + x * 30, int(10 + y * 30 - offset), 30, 30))

            if item == '@':
                screen.blit(snowman, new_location)
            elif item == '#':
                screen.blit(rock, new_location)

    # move skier
    if skier_direction == 'right':
        skier_location += x_speed
        if skier_location > 420:
            skier_location = 420
            # skier_direction = 'left'
        skier_image = ski_right
    else:
        skier_location -= x_speed
        if skier_location < 10:
            skier_location = 10
            # skier_direction = 'right'
        skier_image = ski_left

    # draw skier
    # new_skier_rect = (skier_location, 10, 30, 30)
    screen.blit(skier_image, pygame.Rect(int(skier_location), 10, 30, 30))

    screen.blit(bg, (10, 0, 50, 50), (10, 0, 50, 50))
    screen.blit(update_fps(), (10,0))

    pygame.display.update()

    offset += y_speed
    if offset == 30:
        offset = 0
        hill.append(hill.pop(0))
