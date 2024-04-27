import pygame

pygame.init()
display = pygame.display.set_mode((100, 200), pygame.RESIZABLE)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

