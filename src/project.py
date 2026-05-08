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
    bangs_count = 0
    bangs_color_count = 0
    bangs = ""
    bangs_color = ""
    hair_count = 0
    hair_color_count= 0
    hair = ""
    hair_color = ""
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
                if bangs_decrease_button[1].collidepoint(mouse):
                    if bangs_count == 0:
                        bangs_count = 25
                    else:
                        bangs_count -= 1
                if bangs_increase_button[1].collidepoint(mouse):
                    if bangs_count == 25:
                        bangs_count = 0
                    else:
                        bangs_count += 1
                if bangs_color_decrease_button[1].collidepoint(mouse):
                    if bangs_color_count == 0:
                        bangs_color_count = 15
                    else:
                        bangs_color_count -= 1
                if bangs_color_increase_button[1].collidepoint(mouse):
                    if bangs_color_count == 15:
                        bangs_color_count = 0
                    else:
                        bangs_color_count += 1
                if hair_decrease_button[1].collidepoint(mouse):
                    if hair_count == 0:
                        hair_count = 20
                    else:
                        hair_count -= 1
                if hair_increase_button[1].collidepoint(mouse):
                    if hair_count == 20:
                        hair_count = 0
                    else:
                        hair_count += 1
                if hair_color_decrease_button[1].collidepoint(mouse):
                    if hair_color_count == 0:
                        hair_color_count = 15
                    else:
                        hair_color_count -= 1
                if hair_color_increase_button[1].collidepoint(mouse):
                    if hair_color_count == 15:
                        hair_color_count = 0
                    else:
                        hair_color_count += 1

        background = pygame.image.load(os.path.join("game_graphics", "background.png")).convert()
        screen.blit(background, (0, 0))
        skin_decrease_button = button(os.path.join("game_graphics", "button_decrease.png"), (445, 95), screen)
        skin_increase_button = button(os.path.join("game_graphics", "button_increase.png"), (605, 95), screen)
        bangs_decrease_button = button(os.path.join("game_graphics", "button_decrease.png"), (445, 175), screen)
        bangs_increase_button = button(os.path.join("game_graphics", "button_increase.png"), (605, 175), screen)
        bangs_color_decrease_button = button(os.path.join("game_graphics", "button_decrease.png"), (635, 175), screen)
        bangs_color_increase_button = button(os.path.join("game_graphics", "button_increase.png"), (765, 175), screen)
        hair_decrease_button = button(os.path.join("game_graphics", "button_decrease.png"), (445, 255), screen)
        hair_increase_button = button(os.path.join("game_graphics", "button_increase.png"), (605, 255), screen)
        hair_color_decrease_button = button(os.path.join("game_graphics", "button_decrease.png"), (635, 255), screen)
        hair_color_increase_button = button(os.path.join("game_graphics", "button_increase.png"), (765, 255), screen)
        
        if hair_count == 0:
            blitify("hair1.png", screen)
            hair = "1hair_"
        elif hair_count == 1:
            blitify("hair2.png", screen)
            hair = "2hair_"
        elif hair_count == 2:
            blitify("hair3.png", screen)
            hair = "3hair_"
        elif hair_count == 3:
            blitify("hair4.png", screen)
            hair = "4hair_"
        elif hair_count == 4:
            blitify("hair5.png", screen)
            hair = "5hair_"
        elif hair_count == 5:
            blitify("hair6.png", screen)
            hair = "6hair_"
        elif hair_count == 6:
            blitify("hair7.png", screen)
            hair = "7hair_"
        elif hair_count == 7:
            blitify("hair8.png", screen)
            hair = "8hair_"
        elif hair_count == 8:
            blitify("hair9.png", screen)
            hair = "9hair_"
        elif hair_count == 9:
            blitify("hair10.png", screen)
            hair = "10hair_"
        elif hair_count == 10:
            blitify("hair11.png", screen)
            hair = "11hair_"
        elif hair_count == 11:
            blitify("hair12.png", screen)
            hair = "12hair_"
        elif hair_count == 12:
            blitify("hair13.png", screen)
            hair = "13hair_"
        elif hair_count == 13:
            blitify("hair14.png", screen)
            hair = "14hair_"
        elif hair_count == 14:
            blitify("hair15.png", screen)
            hair = "15hair_"
        elif hair_count == 15:
            blitify("hair16.png", screen)
            hair = "16hair_"
        elif hair_count == 16:
            blitify("hair17.png", screen)
            hair = "17hair_"
        elif hair_count == 17:
            blitify("hair18.png", screen)
            hair = "18hair_"
        elif hair_count == 18:
            blitify("hair19.png", screen)
            hair = "19hair_"
        elif hair_count == 19:
            blitify("hair20.png", screen)
            hair = "20hair_"
        elif hair_count == 20:
            blitify("hair21.png", screen)
            hair = "21hair_"
        
        if hair_color_count == 0:
            blitify("hair_color_black.png", screen)
            hair_color = "black.png"
        elif hair_color_count == 1:
            blitify("hair_color_dark_brown.png", screen)
            hair_color = "dark_brown.png"
        elif hair_color_count == 2:
            blitify("hair_color_brown.png", screen)
            hair_color = "brown.png"
        elif hair_color_count == 3:
            blitify("hair_color_dirty_blond.png", screen)
            hair_color = "dirty_blond.png"
        elif hair_color_count == 4:
            blitify("hair_color_blond.png", screen)
            hair_color = "blond.png"
        elif hair_color_count == 5:
            blitify("hair_color_white.png", screen)
            hair_color = "white.png"
        elif hair_color_count == 6:
            blitify("hair_color_red.png", screen)
            hair_color = "red.png"
        elif hair_color_count == 7:
            blitify("hair_color_orange.png", screen)
            hair_color = "orange.png"
        elif hair_color_count == 8:
            blitify("hair_color_yellow.png", screen)
            hair_color = "yellow.png"
        elif hair_color_count == 9:
            blitify("hair_color_lime.png", screen)
            hair_color = "lime.png"
        elif hair_color_count == 10:
            blitify("hair_color_green.png", screen)
            hair_color = "green.png"
        elif hair_color_count == 11:
            blitify("hair_color_cyan.png", screen)
            hair_color = "cyan.png"
        elif hair_color_count == 12:
            blitify("hair_color_blue.png", screen)
            hair_color = "blue.png"
        elif hair_color_count == 13:
            blitify("hair_color_purple.png", screen)
            hair_color = "purple.png"
        elif hair_color_count == 14:
            blitify("hair_color_lilac.png", screen)
            hair_color = "lilac.png"
        elif hair_color_count == 15:
            blitify("hair_color_pink.png", screen)
            hair_color = "pink.png"

        blitify(f"{hair}{hair_color}", screen)

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
        
        blitify("eyes.png", screen)

        if bangs_count == 0:
            blitify("bangs1.png", screen)
            bangs = "1bangs_"
        elif bangs_count == 1:
            blitify("bangs2.png", screen)
            bangs = "2bangs_"
        elif bangs_count == 2:
            blitify("bangs3.png", screen)
            bangs = "3bangs_"
        elif bangs_count == 3:
            blitify("bangs4.png", screen)
            bangs = "4bangs_"
        elif bangs_count == 4:
            blitify("bangs5.png", screen)
            bangs = "5bangs_"
        elif bangs_count == 5:
            blitify("bangs6.png", screen)
            bangs = "6bangs_"
        elif bangs_count == 6:
            blitify("bangs7.png", screen)
            bangs = "7bangs_"
        elif bangs_count == 7:
            blitify("bangs8.png", screen)
            bangs = "8bangs_"
        elif bangs_count == 8:
            blitify("bangs9.png", screen)
            bangs = "9bangs_"
        elif bangs_count == 9:
            blitify("bangs10.png", screen)
            bangs = "10bangs_"
        elif bangs_count == 10:
            blitify("bangs11.png", screen)
            bangs = "11bangs_"
        elif bangs_count == 11:
            blitify("bangs12.png", screen)
            bangs = "12bangs_"
        elif bangs_count == 12:
            blitify("bangs13.png", screen)
            bangs = "13bangs_"
        elif bangs_count == 13:
            blitify("bangs14.png", screen)
            bangs = "14bangs_"
        elif bangs_count == 14:
            blitify("bangs15.png", screen)
            bangs = "15bangs_"
        elif bangs_count == 15:
            blitify("bangs16.png", screen)
            bangs = "16bangs_"
        elif bangs_count == 16:
            blitify("bangs17.png", screen)
            bangs = "17bangs_"
        elif bangs_count == 17:
            blitify("bangs18.png", screen)
            bangs = "18bangs_"
        elif bangs_count == 18:
            blitify("bangs19.png", screen)
            bangs = "19bangs_"
        elif bangs_count == 19:
            blitify("bangs20.png", screen)
            bangs = "20bangs_"
        elif bangs_count == 20:
            blitify("bangs21.png", screen)
            bangs = "21bangs_"
        elif bangs_count == 21:
            blitify("bangs22.png", screen)
            bangs = "22bangs_"
        elif bangs_count == 22:
            blitify("bangs23.png", screen)
            bangs = "23bangs_"
        elif bangs_count == 23:
            blitify("bangs24.png", screen)
            bangs = "24bangs_"
        elif bangs_count == 24:
            blitify("bangs25.png", screen)
            bangs = "25bangs_"
        elif bangs_count == 25:
            blitify("bangs26.png", screen)
            bangs = "26bangs_"

        if bangs_color_count == 0:
            blitify("bangs_color_black.png", screen)
            bangs_color = "black.png"
        elif bangs_color_count == 1:
            blitify("bangs_color_dark_brown.png", screen)
            bangs_color = "dark_brown.png"
        elif bangs_color_count == 2:
            blitify("bangs_color_brown.png", screen)
            bangs_color = "brown.png"
        elif bangs_color_count == 3:
            blitify("bangs_color_dirty_blond.png", screen)
            bangs_color = "dirty_blond.png"
        elif bangs_color_count == 4:
            blitify("bangs_color_blond.png", screen)
            bangs_color = "blond.png"
        elif bangs_color_count == 5:
            blitify("bangs_color_white.png", screen)
            bangs_color = "white.png"
        elif bangs_color_count == 6:
            blitify("bangs_color_red.png", screen)
            bangs_color = "red.png"
        elif bangs_color_count == 7:
            blitify("bangs_color_orange.png", screen)
            bangs_color = "orange.png"
        elif bangs_color_count == 8:
            blitify("bangs_color_yellow.png", screen)
            bangs_color = "yellow.png"
        elif bangs_color_count == 9:
            blitify("bangs_color_lime.png", screen)
            bangs_color = "lime.png"
        elif bangs_color_count == 10:
            blitify("bangs_color_green.png", screen)
            bangs_color = "green.png"
        elif bangs_color_count == 11:
            blitify('bangs_color_cyan.png', screen)
            bangs_color = "cyan.png"
        elif bangs_color_count == 12:
            blitify("bangs_color_blue.png", screen)
            bangs_color = "blue.png"
        elif bangs_color_count == 13:
            blitify("bangs_color_purple.png", screen)
            bangs_color = "purple.png"
        elif bangs_color_count == 14:
            blitify("bangs_color_lilac.png", screen)
            bangs_color = "lilac.png"
        elif bangs_color_count == 15:
            blitify("bangs_color_pink.png", screen)
            bangs_color = "pink.png"

        blitify(f"{bangs}{bangs_color}", screen)

        pygame.display.flip()
        dt = clock.tick(24)
    pygame.quit()


if __name__ == "__main__":
    main()