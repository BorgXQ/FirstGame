import pygame

width = 960
height = 540
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

# clientNum = 0

class Player():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x, y, width, height)
        self.vel = 0.5

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def move(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.x -= self.vel
        if key[pygame.K_RIGHT]:
            self.x += self.vel
        if key[pygame.K_UP]:
            self.y -= self.vel
        if key[pygame.K_DOWN]:
            self.y += self.vel
        
        self.rect = (self.x, self.y, self.width, self.height)


def redrawWin(win, player):
    win.fill((255, 255, 255))
    player.draw(win)
    pygame.display.update()


def main():
    run = True
    p = Player(50, 50, 50, 100, (0, 255, 0))

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        p.move()
        redrawWin(win, p)

main()