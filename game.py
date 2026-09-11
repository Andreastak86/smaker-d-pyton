import pygame
import random

pygame.init()

WIDTH = 1280
HEIGHT = 720

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Smaker det Pyton?")

clock = pygame.time.Clock()

# Pål tar form
paal_x = WIDTH // 2
paal_y = HEIGHT // 2
paal_width = 60
paal_height = 40
paal_speed = 5

# Mat
food_x = 300
food_y = 200
food_size = 30

foods = {
    "eple": {
        "score": 10,
        "comment": "Rødt, syrlig og godt",
    },
    "dravle": {"score": 5, "comment": "Ikke veldig godt, men la gå!"},
    "gammelost": {"score": -10, "comment": "Uæh! Det smakte pyton!"},
}

current_food = random.choice(list(foods.keys()))

# Poeng
score = 0

font = pygame.font.Font(None, 36)


# MatPrat
food_comment = ""
comment_time = 0
comment_duration = 2000

running = True

while running:
    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            food_x = random.randint(0, WIDTH - food_size)
            food_y = random.randint(0, HEIGHT - food_size)
            current_food = random.choice(list(foods.keys()))

    # Tastatur
    keys = pygame.key.get_pressed()

    if keys[pygame.K_w] or keys[pygame.K_UP]:
        paal_y -= paal_speed

    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        paal_y += paal_speed

    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        paal_x -= paal_speed

    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        paal_x += paal_speed

    if keys[pygame.K_ESCAPE]:
        running = False

    # Kollisjonsbokser
    paal_rect = pygame.Rect(paal_x, paal_y, paal_width, paal_height)

    food_rect = pygame.Rect(food_x, food_y, food_size, food_size)

    # Har Pål matvet?
    if paal_rect.colliderect(food_rect):
        score += foods[current_food]["score"]

        food_comment = foods[current_food]["comment"]
        comment_time = pygame.time.get_ticks()

        print(foods[current_food]["comment"])
        print(f"Score: {score}")

        food_x = random.randint(0, WIDTH - food_size)
        food_y = random.randint(0, HEIGHT - food_size)

        current_food = random.choice(list(foods.keys()))

    # Tegn bakgrunn
    screen.fill((35, 40, 35))

    # Tegn Pål
    pygame.draw.rect(screen, (80, 180, 80), (paal_x, paal_y, paal_width, paal_height))

    # Tegn mat
    pygame.draw.rect(screen, (200, 70, 70), (food_x, food_y, food_size, food_size))

    # Tekst over maten
    food_text = font.render(current_food, True, (255, 255, 255))

    screen.blit(food_text, (food_x, food_y - 30))

    # Score
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))

    screen.blit(score_text, (20, 20))

    if pygame.time.get_ticks() - comment_time < comment_duration:
        comment_text = font.render(food_comment, True, (255, 255, 255))
        screen.blit(comment_text, (20, 60))

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
