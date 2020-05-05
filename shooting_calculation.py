from math import sin, cos, sqrt, radians


class Calculation():
    def __init__(self, sx=2):
        self.sx = sx  # meter
        self.sy = 0  # meter
        self.k_spring = 117  # newton per meter
        self.spring_dis = 0.1  # meter
        self.ball_weight = 0.025  # kilogram
        self.gravity = 9.81  # meter per second square
        self.f_k = 0.2

    def shooting_velocity(self, theta):  # calculate velocity of ball when shooting with theta
        theta = radians(theta)
        velocity = sqrt((self.k_spring * self.spring_dis ** 2 / self.ball_weight) - 2 * self.gravity * self.spring_dis * (sin(theta) + self.f_k * cos(theta)))

        return [velocity * cos(theta), velocity * sin(theta), velocity]  # [Vx, Vy, V]

    def cal_best_theta(self):
        step = 0.5
        i = 45
        Min = 10000
        best_theta = 0

        while i <= 90:
            v = self.shooting_velocity(i)

            # fix x and find the closet y at any theta
            time = self.sx / v[0]
            y = v[1] * time - 0.5 * self.gravity * time ** 2

            if abs(y - self.sy) < Min:
                best_theta = i
                Min = abs(y - self.sy)

            # fix y and find the closet x at any theta
            time = (v[1] + sqrt(v[1] ** 2 - 4 * 0.5 * self.gravity * self.sy)) / (2 * 0.5 * self.gravity)
            x = v[0] * time

            if abs(x - self.sx) < Min:
                best_theta = i
                Min = abs(x - self.sx)

            i += step

        return best_theta

    def plot(self):  # plot value[Sx,Sy,Vx,Vy]
        theta = self.cal_best_theta()
        velocity = self.shooting_velocity(theta)
        time = 0
        data = []
        total_time = self.sx / velocity[0]

        while time <= total_time:  # plot sx,sy,vx,vy at time step by 0.001 sec or 1 milli sec
            data.append([velocity[0] * time, velocity[1] * time - 0.5 * self.gravity * time ** 2, velocity[0], velocity[1] - self.gravity * time])  # [Sx, Sy, Vx, Vy]
            time += 0.001  # step by 1 milli sec

        return data, theta, total_time
