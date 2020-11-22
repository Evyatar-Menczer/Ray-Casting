import pygame
from Light import Light
pygame.font.init()
pygame.init()


def draw_buttons(screen,color):
    travel_button = (50,630,100,50)
    travel_fnt = pygame.font.SysFont("Meta", 30)
    travel_surf = travel_fnt.render("Travel", True, (255,255,255))
    pygame.draw.rect(screen,color,travel_button,0)
    pygame.draw.rect(screen,(255,255,255),travel_button,2)
    screen.blit(travel_surf,(travel_button[0]+ (travel_button[2] / 2 - travel_surf.get_width() // 2),
            travel_button[1] + (travel_button[3] / 2) - travel_surf.get_height() // 2,),)

def draw_stop_travel_label(screen):
    stop_fnt = pygame.font.SysFont("Meta", 30)
    stop_surface = stop_fnt.render("Press Space To Stop Traveling",True,(147,112,219))
    screen.blit(stop_surface,(220,640),)

def if_mouse_on_button(pos):
    darker = (147,112,219)
    lighter = (170,130,250)
    if 150 > pos[0] > 50 and 680 > pos[1] > 630:
        color = lighter
    else:
        color = darker
    return color

def button_clicked(pos,light):
    if 150 > pos[0] > 50 and 680 > pos[1] > 630:
        if not light.travel:
            light.travel = True
        else:
            light.travel = False





if __name__ == '__main__':

    screen = pygame.display.set_mode((700, 700))
    screen.fill((0, 0, 0))
    travel = False
    pygame.display.set_caption("Light Beams")
    light = Light(screen)
    light.create_boundarys()
    is_running = True

    while is_running:
        pos = pygame.mouse.get_pos()
        if pos[1] > 600 and not light.travel:
            pygame.mouse.set_visible(True)
            light.on = False
        else:
            pygame.mouse.set_visible(False)
            light.on = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())
                button_clicked(pos,light)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and light.travel:
                    light.travel = False

        color = if_mouse_on_button(pos)
        if light.travel:
            light.set_pos()
            light.shine()
            draw_stop_travel_label(screen)
        else:
            light.set_pos(pos)
            light.shine()
        draw_buttons(screen,color)
        pygame.display.update()