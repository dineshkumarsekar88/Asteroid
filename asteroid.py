import pygame
import random
from constants import *
from circleshape import CircleShape
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen, color="white"):
        pygame.draw.circle(screen, color, self.position, self.radius, LINE_WIDTH)
        
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        if self.radius > ASTEROID_MIN_RADIUS:
            log_event("asteroid_split")
            #random.uniform(20,50)
            new_velocity1=self.velocity.rotate(random.uniform(20,50))
            new_velocity2=self.velocity.rotate(-random.uniform(20,50))
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            #new_velocity1 = self.velocity.rotate(30)
            #new_velocity2 = self.velocity.rotate(-30)
            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid1.velocity = new_velocity1 * 1.2
            asteroid2.velocity = new_velocity2 * 1.2
            return asteroid1, asteroid2