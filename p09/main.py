# --------------------------------------------------- #
#   * * *   *   *  * * *      *     **    **  * * *   #
#   *   *    * *   *   *     * *    * *  * *  *       #
#   * * *    **    *         * *    *  *   *  * * *   #
#   *        *     *  **    * * *   *  *   *  *       #
#   *       *      * * *   *     *  *      *  * * *   #
# --------------------------------------------------- #

import pygame
import sys

screen_width = 800
screen_height = 600
# ініціалізація pygame
pygame.init()
# створюємо вікно
screen = pygame.display.set_mode((screen_width, screen_height))
# інтервал оновлення екрану
clock = pygame.time.Clock()
clock_tick = 60

# заголовок вікна
pygame.display.set_caption('GTA_SPYDER v0.1')

spyder_img = pygame.image.load('images/spyder.png')
spyder_position = {'x': 10, 'y': 100}

# background = pygame.Surface((screen_width, screen_height))
# background.fill('Black')
background = pygame.image.load('images/background.jpg')

# додати текст
count_fly = pygame.font.Font('fonts/MadimiOne-Regular.ttf', 50)
text_count_fly = count_fly.render('Count: 0', False, 'Black')
# ==============================================================
while True:
    # перевіряємо події які відбулися в системі
    # events = pygame.event.get()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 1. робимо розрахунки
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]: # K_UP
        if spyder_position['y'] > 0:
            spyder_position['y'] -= 4
    if keys[pygame.K_s]: # K_DOWN
        if spyder_position['y'] < screen_height-110:
            spyder_position['y'] += 4
    if keys[pygame.K_a]: # K_LEFT
        if spyder_position['x'] > 0:
            spyder_position['x'] -= 4
    if keys[pygame.K_d]: # K_RIGHT
        if spyder_position['x'] < screen_width-110:
            spyder_position['x'] += 4

    # 2. додаємо обєкти на екран
    screen.blit(background, (0, 0))
    screen.blit(spyder_img, (spyder_position['x'], spyder_position['y']))
    screen.blit(text_count_fly, (600, 10))

    # 3. оновляємо області украну
    pygame.display.update()
    clock.tick(clock_tick)
