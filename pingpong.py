from pygame import *
window = display.set_mode((900, 800))
display.set_caption('PingPong')
timer = time.Clock()

game = True

while game:
    for e in event.get():
        if e.type ==QUIT:
            game = False

    display.update()
    timer.tick(60)