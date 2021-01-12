import pygame
import os
from threading import Timer
if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Движущийся круг 2')
    size = width, height = 800, 400
    screen = pygame.display.set_mode(size)


pygame.init()

size = width, height = 800, 400
screen = pygame.display.set_mode(size)

def hello():
    a = args[0]
    s = args[1]
    if s % 5 == 0:
        Landing(a)
        args[1] = s + 1
        t = Timer(1.5, hello)
        t.start()
    elif s % 5 == 1:
        Landing([a[0] + 80, a[1]])
        args[1] = s + 1
        t = Timer(1.5, hello)
        t.start()
    elif s % 5 == 2:
        Landing([a[0] - 160, a[1]])
        args[1] = s + 1
        t = Timer(1.5, hello)
        t.start()
    elif s % 5 == 3:
        Landing([a[0] + 160, a[1]])
        args[1] = s + 1
        t = Timer(1.5, hello)
        t.start()
    elif s % 5 == 4:
        Landing([a[0] - 80, a[1]])
        args[1] = s + 1
        t = Timer(1.5, hello)
        t.start()

def load_image(name, color_key=None):
    fullname = os.path.join('datamoun', name)
    try:
        image = pygame.image.load(fullname).convert()
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)

    if color_key is not None:
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    else:
        image = image.convert_alpha()
    return image



class Landing(pygame.sprite.Sprite):
    image = load_image("pt.gif")

    def __init__(self, pos):
        super().__init__(all_sprites)
        self.image = Landing.image
        self.rect = self.image.get_rect()
        self.pos = pos
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self):
        self.rect = self.rect.move(0, -1)


all_sprites = pygame.sprite.Group()


clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            a = 400, 400
            s = 0
            args = [a, s]
            hello()
    real_pos = pygame.mouse.get_pos()
    # print(pos[1])
    if real_pos[1] < 100:
        pos = (real_pos[0], 100)
    else:
        pos = (real_pos[0], real_pos[1])
    pygame.draw.circle(screen, (0, 0, 255), pos, 20)
    screen.fill(pygame.Color((178, 250, 255)))
    all_sprites.draw(screen)
    all_sprites.update()
    pygame.display.flip()
    clock.tick(50)
pygame.quit()


