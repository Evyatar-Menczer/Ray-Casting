import math
import pygame
from Boundary import Boundary
from Ray import Ray
from random import randint
from noise import pnoise1

class Light:

    def __init__(self,screen):
        self.screen = screen
        self.pos = (350,300)
        self.boundarys = []
        self.rays = []
        for i in range(0, 361, 1):
            radian = math.radians(i)
            x = self.pos[0] + math.cos(radian)*2
            y = self.pos[1] + math.sin(radian)*2
            r = Ray(screen,self.pos,(x, y),self.boundarys)
            r.beam()
            self.rays.append(r)
        self.on = True
        self.x_offset = 10000
        self.y_offset = 400
        self.travel = False

    def create_boundarys(self):
        width = pygame.display.Info().current_w
        height = pygame.display.Info().current_h

        top = Boundary(self.screen,(0,0),(width,0))
        left = Boundary(self.screen,(0,0),(0,height-100))
        right = Boundary(self.screen,(width,0),(width,height-100))
        bottom = Boundary(self.screen,(0,height-100),(width,height-100))
        self.boundarys.append(top)
        self.boundarys.append(left)
        self.boundarys.append(right)
        self.boundarys.append(bottom)


        for i in range(6):
            b = Boundary(self.screen,(randint(0,width),randint(0,height - 100)),(randint(0,width),randint(0,height - 100)))
            self.boundarys.append(b)
            b.draw_boundary()

    def set_pos(self, new_pos=None):
        width = pygame.display.Info().current_w
        height = pygame.display.Info().current_h
        if new_pos:
            self.pos = new_pos
        else:
            self.pos = (abs(pnoise1(self.x_offset) * width), abs(pnoise1(self.y_offset) * height))
            self.x_offset += 0.003
            self.y_offset += 0.003

        for ray in self.rays:
            ray.start = self.pos

    def shine(self):
        if self.on:
            self.screen.fill((0, 0, 0))
            k = 0
            for i in range(0, 361, 1):
                radian = math.radians(i)
                dir_x = self.pos[0] + math.cos(radian) * 2
                dir_y = self.pos[1] + math.sin(radian) * 2
                self.rays[k].direction = (dir_x,dir_y)
                self.rays[k].beam()
                k += 1
        else:
            self.screen.fill((0, 0, 0))
            for b in self.boundarys:
                b.draw_boundary()

