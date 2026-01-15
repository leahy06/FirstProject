import pygame
import random

'''
FirstPygame project/lab, a swuare chasing game
__author__ = "Leah Yang"
01/15/2026
'''
def main():
    #Initialize pygame
    pygame.init()

    BLUE = (0, 0, 255)
    RED = (255, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    BLACK = (0, 0, 0)


    #while speed_x==0 or speed_y==0:
    speed_x = random.randint(-9,9)# moves 5 pixels right each frame
    speed_y = random.randint(-9,9)  # not moving vertically yet

    size=(1000, 800)

    #setup the screen
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("LEAH")
    #keep the animation loop going
    running = True

    # this is a Rect object in Pygame--draw to the screen
    mainRect = pygame.Rect(random.randint(0, size[0]-100), random.randint(0, size[1]-100), 100, 100)
    playerRect=pygame.Rect((size[0]-10)/2, (size[1]-10)/2, 20, 20)
    clock=pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            playerRect.move_ip(-2,0)
        if keys[pygame.K_RIGHT]:
            playerRect.move_ip(2,0)
        if keys[pygame.K_UP]:
            playerRect.move_ip(0,-2)
        if keys[pygame.K_DOWN]:
            playerRect.move_ip(0,2)

        playerRect.clamp_ip(screen.get_rect())

        # 0-255 2^8 = RGB  0000 0000 1111 1111
        screen.fill(BLACK)
        pygame.draw.rect(screen, BLUE, mainRect)
        pygame.draw.rect(screen, RED, playerRect)

        pygame.display.flip()
        mainRect.x += speed_x
        mainRect.y += speed_y

        if mainRect.right>size[0] or mainRect.left<0:
            speed_x *= -1
        if mainRect.bottom>size[1] or mainRect.top<0:
            speed_y *= -1
        clock.tick(120)

        if mainRect.colliderect(playerRect):
            running = False
    running=True
    font = pygame.font.Font(None, 62)
    text_surface=font.render("GAME OVER, CLICK TO QUIT", True, RED)
    text_rect=text_surface.get_rect(center=(size[0]//2, size[1]//2))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                running = False
        screen.fill(BLACK)
        screen.blit(text_surface, text_rect)
        pygame.display.flip()
    pygame.quit()

if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
