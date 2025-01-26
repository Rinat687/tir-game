import pygame
import random
import sys

# Инициализация Pygame
pygame.init()

# Настройки игры
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
TARGET_SIZE = 60
TARGET_IMAGE_PATH = "img/target.png"
ICON_IMAGE_PATH = "img/icon.jpg"

# Цвета
COLOR = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Настройка экрана
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Игра Тир")

# Загрузка иконки
try:
    icon = pygame.image.load(ICON_IMAGE_PATH)
    pygame.display.set_icon(icon)
except FileNotFoundError:
    print(f"Ошибка: Файл иконки {ICON_IMAGE_PATH} не найден.")

# Загрузка изображения мишени
try:
    target_img = pygame.image.load(TARGET_IMAGE_PATH)
    target_img = pygame.transform.scale(target_img, (TARGET_SIZE, TARGET_SIZE))
except FileNotFoundError:
    print(f"Ошибка: Файл мишени {TARGET_IMAGE_PATH} не найден.")
    sys.exit()

# Начальная позиция мишени
target_x = random.randint(0, SCREEN_WIDTH - TARGET_SIZE)
target_y = random.randint(0, SCREEN_HEIGHT - TARGET_SIZE)

# Счетчик попаданий
score = 0

# Шрифт для отображения счета
font = pygame.font.Font(None, 36)

# Основной цикл игры
clock = pygame.time.Clock()
running = True

while running:
    screen.fill(COLOR)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + TARGET_SIZE and target_y < mouse_y < target_y + TARGET_SIZE:
                target_x = random.randint(0, SCREEN_WIDTH - TARGET_SIZE)
                target_y = random.randint(0, SCREEN_HEIGHT - TARGET_SIZE)
                score += 1
                # Здесь можно добавить звук попадания

    # Отображение мишени
    screen.blit(target_img, (target_x, target_y))

    # Отображение счета
    score_text = font.render(f"Счет: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    # Обновление экрана
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()