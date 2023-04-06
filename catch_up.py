from pygame import *

WIDTH,HEIGHT = 700, 500  
FPS = 60

window = display.set_mode((WIDTH, HEIGHT))
display.set_caption("Доганялки")
bg = transform.scale(image.load("background.png"), (WIDTH, HEIGHT))
sprite1 = transform.scale(image.load("sprite1.png"), (70, 70))
x1, y1 = 40,350
sprite2 = transform.scale(image.load("sprite2.png"), (70, 70))
x2, y2 = WIDTH - 100, 350

run = True
clock = time.Clock()

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    pressed = key.get_pressed()
    if pressed[K_UP] and y2 > 0:
        y2 -= 3
    if pressed[K_DOWN] and y2 < HEIGHT - 70:
        y2 += 3
    if pressed[K_LEFT] and x2 > 0:
        x2 -= 3
    if pressed[K_RIGHT] and x2 < WIDTH - 70:
        x2 += 3

    if pressed[K_w] and y1 > 0:
        y1 -= 3
    if pressed[K_s] and y1 < HEIGHT - 70:
        y1 += 3
    if pressed[K_a] and x1 > 0:
        x1 -= 3
    if pressed[K_d] and x1 < WIDTH - 70:
        x1 += 3

    window.blit(bg, (0, 0))
    window.blit(sprite1, (x1, y1))
    window.blit(sprite2, (x2, y2))

    display.update()
    clock.tick(FPS)
    
