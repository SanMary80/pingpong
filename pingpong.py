from pygame import *
window = display.set_mode((900, 800))
display.set_caption('PingPong')
timer = time.Clock()

class Sprite(sprite.Sprite):
    def __init__(self, image_file, width, height, x, y):
        super().__init__()
        self.image = transform.scale(image.load(image_file),(width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(Sprite):
    def __init__(self, image_file, width, height, x, y, k_up, k_down, speed):
        super().__init__(image_file, width, height, x, y)
        self.k_up = k_up
        self.k_down = k_down
        self.speed = speed
    def update(self):
        keys = key.get_pressed()
        if keys[self.k_up]:
            self.rect.y -= self.speed
        if keys[self.k_down]:
            self.rect.y += self.speed
class Ball(Sprite):
    def __init__(self, image_file, width, height, x, y, speed):
        super().__init__(image_file, width, height, x, y)
        self.speed_x = speed
        self.speed_y = speed
    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

player_1 = Player('platform_30x200.png', 30, 200, 10, 400, K_w, K_s, 3)
player_2 = Player('platform_30x200.png', 30, 200, 800, 400, K_UP, K_DOWN, 3)
ball = Ball('ball_100x100.png', 100, 100, 400, 400, 4)
game = True
platforms = sprite.Group(player_1, player_2)

while game:
    window.fill((50, 200, 250))
    for e in event.get():
        if e.type ==QUIT:
            game = False
    platforms.update()
    ball.update()
    platforms.draw(window)
    ball.reset()
    display.update()
    timer.tick(60)