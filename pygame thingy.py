import pygame

# pygame setup
pygame.init()
WIDTH = 1280
HEIGHT = 720
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
GRAVITY = 500
JUMP_STRENGTH = -300

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
player_velocity = 0
canjump = True


class Player(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.size = (100, 100)
        self.big_image = pygame.image.load("Bird.png").convert()  
        self.big_image.set_colorkey((255,255,255))  
        self.image = pygame.transform.scale(self.big_image, self.size)

    def draw(self, position):
        screen.blit(self.image, (int(position.x), int(position.y)))
        self.rect = pygame.Rect(int(position.x)+ 13, int(position.y) + 20, 70, 60) # adjustments to rect
        pygame.draw.rect(screen, "red", background_rect, 3)
  



background_surface = pygame.image.load("Background.png")
background_surface = pygame.transform.scale(background_surface,(1280,720))
background_rect = pygame.Rect(0,660, WIDTH,1)



flappy = Player()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and canjump:
                player_velocity = JUMP_STRENGTH
                canjump = False

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                canjump = True

    # Apply gravity
    player_velocity += GRAVITY * dt
    player_pos.y += player_velocity * dt

    # Prevent falling through the floor
    if player_pos.y >= screen.get_height() - 100:
        player_pos.y = screen.get_height() - 100
        player_velocity = 0
        canjump = True

    # Drawing
    screen.fill("white")
    screen.blit(background_surface,(0,0))

    flappy.draw(player_pos)
    
    pygame.display.flip()

    dt = clock.tick(60) / 1000  # Maintain consistent frame timing

pygame.quit()
