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

# Poeng
score = 0
font = pygame.font.Font(None, 36)

running = True

while running:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

   
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

   

    paal_rect = pygame.Rect(
        paal_x,
        paal_y,
        paal_width,
        paal_height
    )

    food_rect = pygame.Rect(
        food_x,
        food_y,
        food_size,
        food_size
    )

    # 4. Har Pål matvet?
    if paal_rect.colliderect(food_rect):
        score += 10
        print(f"Nam. Pål digget den! Score: {score}")

        food_x = random.randint(0, WIDTH - food_size)
        food_y = random.randint(0, HEIGHT - food_size)

  
    screen.fill((35, 40, 35))

    pygame.draw.rect(
        screen,
        (80, 180, 80),
        (paal_x, paal_y, paal_width, paal_height)
    )

    pygame.draw.rect(
        screen,
        (200, 70, 70),
        (food_x, food_y, food_size, food_size)
    )

    
    score_text = font.render(
        f"Score: {score}",
        True,
        (255, 255, 255)
    )

    screen.blit(score_text, (20, 20))


    pygame.display.flip()

  
    clock.tick(60)

pygame.quit()