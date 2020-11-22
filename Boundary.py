import pygame

class Boundary:

    def __init__(self,screen,start_point,end_point):
        self.screen = screen
        self.start_point = start_point
        self.end_point = end_point

    def draw_boundary(self):
        pygame.draw.line(self.screen,(255,0,255),self.start_point,self.end_point,2)
