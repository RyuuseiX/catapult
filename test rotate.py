import pygame as pg
import math
from shooting_calculation import Calculation

pg.init()


win_x, win_y = 1440, 768
posiX, posiY = 50, 600
posiX2 = 1220
Screen = pg.display.set_mode((win_x, win_y))
# setting
radius = 5  # ball radius
Sx = 4  # from launch point to target center
S_bucket = Sx - 0.6035  # from launch point to nearest target
cal = Calculation(S_bucket)
rpm = 90  # round per minute
degree_per_frame = (rpm*0.001) / 60
Pxs = 200  # x pixel : 1 meter *side view
Pxt = 150  # x pixel : 1 meter *top view

S_bucket_Pxs = S_bucket * Pxs
S_bucket_Pxt = S_bucket * Pxt

side_path = './pic/side.png'
top_path = './pic/top.png'
side = pg.image.load(side_path).convert()
top = pg.image.load(top_path).convert()
side = pg.transform.scale(side, (int(1.36 * Pxs), int(0.5 * Pxs)))
top = pg.transform.scale(top, (int(1.36 * Pxt),int(1.36 * Pxt)))

black = (0, 0, 0)
white = (255, 255, 255)
gray = (200, 200, 200)
light_gray = (230, 230, 230)
green = (0, 200, 0)
red = (200, 0, 0)

angle = 0

while 1:
    print(angle)

    Screen.fill(white)
    rot_top = pg.transform.rotate(top, angle)
    Screen.blit(rot_top, (posiX2 - 1.36 * Pxt / 2, 750 - posiX - (Sx + 0.6035) * Pxt))
    if angle < 360:
        angle += degree_per_frame
    else:
        angle -= 360

    pg.time.delay(1)

    pg.display.update()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
