import pygame as pg
from shooting_calculation import Calculation
from text import Text
from button import Button

pg.init()

win_x, win_y = 1440, 768
posiX, posiY = 50, 600
posiX2 = 1220
Screen = pg.display.set_mode((win_x, win_y))

# color
black = (0, 0, 0)
white = (255, 255, 255)
gray = (200, 200, 200)
light_gray = (230, 230, 230)
green = (0, 200, 0)
red = (200, 0, 0)

# setting
radius = 5  # ball radius
Sx = 4  # from launch point to target center
S_bucket = Sx - 0.6035  # from launch point to nearest target
cal = Calculation(S_bucket)

rpm = 90  # round per minute
degree_per_frame = rpm * 0.001 / 60 * 360

speed = 1  # view speed
speed_btn = Button(950, 40, 70, 50)

Pxs = 200  # x pixel : 1 meter *side view
Pxt = 150  # x pixel : 1 meter *top view

S_bucket_Pxs = S_bucket * Pxs
S_bucket_Pxt = S_bucket * Pxt

# bucket image path
side_path = './pic/side.png'
top_path = './pic/top.png'
side = pg.image.load(side_path)
top = pg.image.load(top_path)
side = pg.transform.scale(side, (int(1.364 * Pxs), int(0.5 * Pxs)))

data, theta, total_time = cal.plot()  # data = [Sx, Sy, Vx, Vy, V] *s from launch point
angle = 0

print(total_time)

while 1:
    launch = False
    launch_time = 0
    wait_time = 1 / (rpm / 60) - total_time
    if wait_time <= 0:
        wait_time += 1 / (rpm / 60)
    print(wait_time)
    time = 0
    plot = 0

    while plot < len(data):
        if launch is False:  # wait for the right time
            plot = 0

        Screen.fill(white)

        # text
        Sx_txt = Text(Screen, 'Sx = ' + '%.3f' % data[plot][0] + ' meter', 20)
        Sx_txt.write_tl(40, 40)
        Sy_txt = Text(Screen, 'Sy = ' + '%.3f' % data[plot][1] + ' meter', 20)
        Sy_txt.write_tl(40, 60)
        Vx_txt = Text(Screen, 'Vx = ' + '%.3f' % data[plot][2] + ' meter/sec', 20)
        Vx_txt.write_tl(40, 80)
        Vy_txt = Text(Screen, 'Vy = ' + '%.3f' % data[plot][3] + ' meter/sec', 20)
        Vy_txt.write_tl(40, 100)
        V_txt = Text(Screen, 'V = ' + '%.3f' % data[plot][4] + ' meter/sec', 20)
        V_txt.write_tl(40, 120)
        angle_txt = Text(Screen, 'angle = ' + str(theta) + ' degree', 20)
        angle_txt.write_tl(40, 140)
        time_txt = Text(Screen, 'time = ' + '%.3f' % time + ' sec', 20)
        time_txt.write_tl(40, 160)

        # button
        speed_btn.draw(Screen, 'x' + str(speed))

        if speed_btn.isMouseOn():
            if pg.mouse.get_pressed()[0] == 1:
                if speed > 0.25:
                    speed -= 0.25
                elif speed == 0.25:
                    speed = 1

                pg.time.delay(100)  # debounced button

        pg.draw.line(Screen, red, (1050, 0), (1050, 768), 2)  # line between side and top view

        # bucket
        Screen.blit(side, (posiX + S_bucket_Pxs - 0.0785 * Pxs, posiY))  # side
        rot_top = pg.transform.rotate(top, angle)
        Screen.blit(rot_top, (posiX2 - int(rot_top.get_width()) / 2, 770 - posiX - int(rot_top.get_height() / 2) - Sx * Pxt))  # top

        angle += degree_per_frame if angle < 360 else - 360 + degree_per_frame

        if launch_time >= wait_time:
            launch = True

        # ball
        pg.draw.circle(Screen, red, (posiX, posiY), radius)
        pg.draw.circle(Screen, black, (posiX + Pxs * data[plot][0], posiY - Pxs * data[plot][1]), radius)  # side
        pg.draw.circle(Screen, red, (posiX2, 770 - posiX), radius) #
        pg.draw.circle(Screen, black, (posiX2, 770 - posiX - data[plot][0] * Pxt), radius)  # top

        time += 0.001
        launch_time += 0.001
        plot += 1

        pg.time.delay(int(1 / speed))

        pg.display.update()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()

    pg.time.delay(1000)


