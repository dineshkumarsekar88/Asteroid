import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from logger import log_event, log_state
from circleshape import *
from shot import Shot
pygame.init()
clock=pygame.time.Clock()
dt=0


def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids= pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)
    Player.containers = (updatable, drawable)
    
    asteroidfield = AsteroidField()
    player=Player(x,y)
    print("Starting Asteroids with pygame version:", pygame.version.ver)
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        dt = clock.tick(60) / 1000.0
        #print ("Delta time (seconds):", dt)
        for drawables in drawable:
            drawables.draw(screen)
        updatable.update(dt)
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    asteroid.split()
                    shot.kill()
            if player.collides_with(asteroid):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        pygame.display.flip()



if __name__ == "__main__":
    main()
