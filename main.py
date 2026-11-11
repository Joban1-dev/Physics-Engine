import pygame as pg
from sys import exit
from engine_logic import PhysicsObject, PhysicsWorld
import random

WIDTH = 800
HEIGHT = 600
screen = pg.display.set_mode((WIDTH,HEIGHT))
clock = pg.Clock()
environment = PhysicsWorld(screen)
frame_rate = 60
environment.add_object(100)

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                pg.quit()
                exit()
            if event.key == pg.K_RETURN:
                environment.add_object(1)

    screen.fill((0,0,0))

    environment.update()

    pg.display.flip()
    clock.tick(frame_rate)
