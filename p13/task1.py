# x: int = 12
# s: str = "string"
class Ball:
    color: tuple = (0, 0, 0)
    radius: int = 0
    weight: float = 0
    x: int = 0
    y: int = 0
    speed_x: int = 0
    speed_y: int = 0
    def __init__(self, radius: int, weight: float):
        if radius > 0:
            self.radius = radius
        else:
            print('Error! radius cannot less zero')
        if weight > 0:
            self.weight = weight
        else:
            print('Error! weight cannot less zero')
    # def Ball(color, radius, weight, x, y, speed_x, speed_y):
    #     pass
    def move_x(self, speed_x: int = 0):
        if speed_x > 0:
            self.x += self.speed_x

    def move_y(self):
        self.y += self.speed_y



ball_1 = Ball(5, 20)

# ball_2 = Ball()
# print(type(ball_1))
# print((type(1)))
# ball_1.radius = 23
ball_1.speed_x = 1
ball_1.move_x()
ball_1.speed_x = 20
ball_1.move_x(ball_1.speed_x)
print(ball_1.radius)