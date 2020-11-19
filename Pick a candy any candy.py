import pygame
import random

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
yellow = (255,255,0)




screen_width = 637
screen_height = 800


class Block(pygame.sprite.Sprite):

    def __init__(self,filename):

        super().__init__()

        self.image = pygame.image.load(filename).convert()

        self.image.set_colorkey(black)

        self.rect = self.image.get_rect()

        
pygame.init()

screen = pygame.display.set_mode([screen_width,screen_height])
pygame.display.set_caption("Candy Collector")

background_image = pygame.image.load("halloween.jpg").convert()
background_position = [0,0]

block_list = pygame.sprite.Group()
all_sprite_list = pygame.sprite.Group()



for i in range(600):

    block = Block("sweet.png")

    block.rect.x = random.randrange(screen_width)
    block.rect.y = random.randrange(screen_height)


    block_list.add(block)


    all_sprite_list.add(block)


player = Block("bagy.png")
all_sprite_list.add(player)


pygame.mixer.music.load("spooky.ogg")
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.1)



running = True
clock = pygame.time.Clock()
score = 0


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background_image, background_position)


    pos = pygame.mouse.get_pos()

    player.rect.x = pos[0]
    player.rect.y = pos[1]

    block_hit_list = pygame.sprite.spritecollide(player, block_list, True)

    for block in block_hit_list:
        score += 1
        print("Dear Player You have Collected " + str(score) + " candie(s) so far from space!")

    all_sprite_list.draw(screen)


    pygame.display.flip()

    clock.tick(60)
    



pygame.quit()

