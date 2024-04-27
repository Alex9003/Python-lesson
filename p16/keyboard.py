import pygame

pygame.init()
display = pygame.display.set_mode((300, 300), pygame.OPENGL)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            key = pygame.key.name(event.key)
            print('Down:  ', key)
        if event.type == pygame.KEYUP:
            key = pygame.key.name(event.key)
            print('Up:  ', key)
