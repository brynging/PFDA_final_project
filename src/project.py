import pygame
import os

def button(graphic, coords, surface):
    image = pygame.image.load(graphic).convert_alpha()
    imagerect = image.get_rect()
    imagerect.topright = coords
    surface.blit(image, imagerect)
    return (image, imagerect)

def blitify(graphic, surface):
    surface.blit(pygame.image.load(os.path.join("game_graphics", graphic)).convert_alpha(), (0, 0))

def main():
    pygame.init()
    pygame.display.set_caption("Character Creator")
    clock = pygame.time.Clock()
    dt = 0
    resolution = (800, 600)
    screen = pygame.display.set_mode(resolution)
    skin_count = 3
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse = pygame.mouse.get_pos()
                if skin_decrease_button[1].collidepoint(mouse):
                    if skin_count == 0:
                        skin_count = 6
                    else:
                        skin_count -= 1
                if skin_increase_button[1].collidepoint(mouse):
                    if skin_count == 6:
                        skin_count = 0
                    else:
                        skin_count += 1
        background = pygame.image.load(os.path.join("game_graphics", "background.png")).convert()
        screen.blit(background, (0, 0))
        skin_decrease_button = button(os.path.join("game_graphics", "button_decrease.png"), (445, 95), screen)
        skin_increase_button = button(os.path.join("game_graphics", "button_increase.png"), (605, 95), screen)

        if skin_count == 0:
            blitify("darkest.png", screen)
            blitify("skin_darkest.png", screen)
        elif skin_count == 1:
            blitify("darker.png", screen)
            blitify("skin_darker.png", screen)
        elif skin_count == 2:
            blitify("dark.png", screen)
            blitify("skin_dark.png", screen)
        elif skin_count == 3:
            blitify("medium.png", screen)
            blitify("skin_medium.png", screen)
        elif skin_count == 4:
            blitify("light.png", screen)
            blitify("skin_light.png", screen)
        elif skin_count == 5:
            blitify("lighter.png", screen)
            blitify("skin_lighter.png", screen)
        elif skin_count == 6:
            blitify("lightest.png", screen)
            blitify("skin_lightest.png", screen)

        pygame.display.flip()
        dt = clock.tick(24)
    pygame.quit()


if __name__ == "__main__":
    main()