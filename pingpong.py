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



game = True

while game:
    for e in event.get():
        if e.type ==QUIT:
            game = False

    display.update()
    timer.tick(60)