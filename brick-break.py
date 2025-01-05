import pygame
import sys

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Brick Breaker")

clock = pygame.time.Clock()

class Paddle:
    def __init__(self):
        self.width = 100
        self.height = 10
        self.x = (SCREEN_WIDTH - self.width) // 2
        self.y = SCREEN_HEIGHT - 30
        self.color = BLUE
        self.speed = 10

    def move_left(self):
        self.x -= self.speed
        if self.x < 0:
            self.x = 0

    def move_right(self):
        self.x += self.speed
        if self.x > SCREEN_WIDTH - self.width:
            self.x = SCREEN_WIDTH - self.width

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

class Ball:
    def __init__(self):
        self.radius = 10
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT // 2
        self.color = GREEN
        self.speed_x = 5
        self.speed_y = -5

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y
        if self.x - self.radius <= 0 or self.x + self.radius >= SCREEN_WIDTH:
            self.speed_x = -self.speed_x
        if self.y - self.radius <= 0:
            self.speed_y = -self.speed_y
        if self.y + self.radius >= SCREEN_HEIGHT:
            return False
        return True

    def reset(self):
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT // 2
        self.speed_y = -self.speed_y

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

class Brick:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = YELLOW
        self.is_broken = False

    def draw(self, screen):
        if not self.is_broken:
            pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
            pygame.draw.rect(screen, BLACK, (self.x, self.y, self.width, self.height), 2)

def create_bricks(rows, cols):
    bricks = []
    brick_width = SCREEN_WIDTH // cols
    brick_height = 20
    for row in range(rows):
        for col in range(cols):
            x = col * brick_width
            y = row * brick_height
            brick = Brick(x, y, brick_width, brick_height)
            bricks.append(brick)
    return bricks

def check_collision(ball, paddle, bricks):
    if (paddle.y <= ball.y + ball.radius <= paddle.y + paddle.height and
            paddle.x <= ball.x <= paddle.x + paddle.width):
        ball.speed_y = -ball.speed_y
    for brick in bricks:
        if not brick.is_broken:
            if (brick.y <= ball.y - ball.radius <= brick.y + brick.height and
                    brick.x <= ball.x <= brick.x + brick.width):
                ball.speed_y = -ball.speed_y
                brick.is_broken = True
                return True
    return False

def draw_score_and_lives(screen, score, lives):
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    heart_image = pygame.Surface((30, 30), pygame.SRCALPHA)
    pygame.draw.polygon(heart_image, RED, [(15, 0), (30, 15), (15, 30), (0, 15)], 0)
    heart_image = pygame.transform.scale(heart_image, (30, 30))
    for i in range(lives):
        screen.blit(heart_image, (SCREEN_WIDTH - 120 + i * 40, 10))

def game_over_screen():
    font = pygame.font.Font(None, 74)
    text = font.render("GAME OVER", True, RED)
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    screen.blit(text, text_rect)
    pygame.display.flip()
    pygame.time.wait(3000)

def game_cleared_screen():
    font = pygame.font.Font(None, 74)
    text = font.render("GAME CLEARED", True, GREEN)
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    screen.blit(text, text_rect)
    pygame.display.flip()
    pygame.time.wait(3000)

def main():
    paddle = Paddle()
    ball = Ball()
    bricks = create_bricks(5, 10)
    score = 0
    lives = 3
    running = True
    game_cleared = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            paddle.move_left()
        if keys[pygame.K_RIGHT]:
            paddle.move_right()

        if not ball.move():
            lives -= 1
            ball.reset()
            if lives <= 0:
                game_over_screen()
                break

        if check_collision(ball, paddle, bricks):
            score += 1

        if not game_cleared and all(brick.is_broken for brick in bricks):
            game_cleared = True
            game_cleared_screen()
            break

        screen.fill(BLACK)
        paddle.draw(screen)
        ball.draw(screen)
        for brick in bricks:
            brick.draw(screen)
        draw_score_and_lives(screen, score, lives)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
