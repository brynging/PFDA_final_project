import pygame
import os

def button(graphic, coords, surface):
    image = pygame.image.load(graphic).convert_alpha()
    imagerect = image.get_rect()
    imagerect.topright = coords
    surface.blit(image, imagerect)
    return (image, imagerect)

def main():
    pygame.init()
    pygame.display.set_caption("Character Creator")
    clock = pygame.time.Clock()
    dt = 0
    resolution = (800, 600)
    screen = pygame.display.set_mode(resolution)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse = pygame.mouse.get_pos()
                if skin_decrease_button[1].collidepoint(mouse):
                    print("Button pressed!")
        background = pygame.image.load(os.path.join("game_graphics", "background.png")).convert()
        screen.blit(background, (0, 0))
        skin_decrease_button = button(os.path.join("game_graphics", "button_decrease.png"), (435, 95), screen)

        pygame.display.flip()
        dt = clock.tick(24)
    pygame.quit()


if __name__ == "__main__":
    main()