import pygame as pg
import math

pg.init()
Screen = pg.display.set_mode((1440, 768))  # 1 สร้างหน้าต่างเกม

black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 200, 0)
red = (200, 0, 0)
theta = 30
theta = math.radians(theta)

while 1:  # 2 ทำการสร้าง loop
    Screen.fill(white)
    pg.draw.line(Screen, black, (10,600 * math.cos(theta)), (30, 600))
    # pg.draw.polygon(Screen, green, ((10, 600), (10, 30)), 20)

    pg.time.delay(1)  # หน่วงเวลา

    pg.display.update()  # 4 ทำการอัพเดท

    for event in pg.event.get():  # ทำการ Check event ต่างๆที่เกิดขึ้น
        if event.type == pg.QUIT:
            pg.quit()
            exit()
