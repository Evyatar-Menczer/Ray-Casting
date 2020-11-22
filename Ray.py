import math
import pygame


class Ray:

    def __init__(self,screen,start,direction,boundarys):
        self.screen = screen
        self.start = start
        self.direction = direction
        self.boundarys = boundarys

    def beam(self):
        intersect_pts = []
        for boundary in self.boundarys:
            boundary.draw_boundary()
            intersect_pt = self.if_intersect(boundary)
            if intersect_pt:
                intersect_pts.append(intersect_pt)

        if len(intersect_pts) != 0:
            shortest_distance = math.inf
            shortest_distance_pt = None
            for pt in intersect_pts:
                pt_intr_dist = math.sqrt(((abs(self.start[0]- pt[0]))**2)+((abs(self.start[1]- pt[1]))**2))
                if pt_intr_dist < shortest_distance:
                    shortest_distance = pt_intr_dist
                    shortest_distance_pt = pt
            pygame.draw.line(self.screen, (255, 255, 255),self.start, shortest_distance_pt, 1)

    def if_intersect(self, boundary):
        x1 = boundary.start_point[0]
        y1 = boundary.start_point[1]
        x2 = boundary.end_point[0]
        y2 = boundary.end_point[1]

        x3 = self.start[0]
        y3 = self.start[1]
        x4 = self.direction[0]
        y4 = self.direction[1]

        numerator_t = (x1 - x3)*(y3 - y4)-(y1-y3)*(x3-x4)
        numerator_u = (x1 - x2)*(y1 - y3)-(y1-y2)*(x1-x3)
        denominator = (x1 - x2)*(y3 - y4)-(y1-y2)*(x3-x4)
        if denominator == 0:
            return
        t = numerator_t/denominator
        u = -(numerator_u/denominator)

        if 1 > t > 0 and u > 0:
            intersect_x = x1 + t*(x2 - x1)
            intersect_y = y1 + t*(y2 - y1)
            return int(intersect_x),int(intersect_y)
        else:
            return