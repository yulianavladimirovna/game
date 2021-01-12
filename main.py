import pygame

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Движущийся круг 2')
    size = width, height = 800, 400
    screen = pygame.display.set_mode(size)

    running = True
    clock = pygame.time.Clock()

while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    real_pos = pygame.mouse.get_pos()
    #print(pos[1])
    if real_pos[1] < 100:
        pos = (real_pos[0], 100)
    else:
        pos = (real_pos[0], real_pos[1])
    pygame.draw.circle(screen, (0, 0, 255), pos, 20)
    pygame.display.flip()
    clock.tick(50)