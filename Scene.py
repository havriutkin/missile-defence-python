import math
import random

import pygame

from DefenceSystem import DefenceSystem
from Missile import Missile
from Settings import Settings


class Scene:
    def __init__(self, settings: Settings):
        self.settings = settings  # Get settings

        # Set up pygame
        pygame.init()
        pygame.display.set_caption("Air Defence Simulator")
        self.screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
        self.clock = pygame.time.Clock()
        self.running = False

        # Create one missile
        self.missile = Missile(settings, ([0, 0, 0.1, 0], [-0.00000000625, 0.000075, -0.2, 300]),
                               self.clock, (214, 40, 40))

        # Create defence system
        self.defence = DefenceSystem(settings, self.clock)

        self.sound = pygame.mixer.Sound('res/explosion.mp3')

    def start(self):
        self.running = True
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        # Launch missile if enough observations
                        self.defence.launch_missile()
                        self.defence.observations = []

            self.update()
            self.render()

    def update(self):
        # Add observation to defence system with prob 2/3
        if random.randint(0, 2) in [0, 1]:
            noise_x = random.uniform(-2, 2)
            noise_y = random.uniform(-2, 2)
            self.defence.add_observation(self.missile.t_cur, self.missile.x + noise_x, self.missile.y + noise_y)

        # Check if defence missile blows up
        for defMiss in self.defence.missiles:
            if defMiss.is_blown_up:
                # Find distance between defence and attack missiles
                distance = math.sqrt((self.missile.x - defMiss.x)**2 + (self.missile.y - defMiss.y)**2)

                if distance < 5:
                    self.refresh_objects()
                    self.sound.play()

                self.defence.missiles.remove(defMiss)
                self.sound.play()

        # Update attack missile
        self.missile.update()
        if self.missile.out_of_screen():
            self.refresh_objects()

        # Update defence system
        self.defence.update()

    def render(self):
        self.screen.fill((0, 48, 73))  # Clear the screen

        # Render everything
        self.missile.render(self.screen)
        self.defence.render(self.screen)

        pygame.display.flip()
        self.clock.tick(self.settings.fps)

    def refresh_objects(self):
        self.missile = Missile(self.settings, ([0, 0, 0.1, 0], [-0.00000000625, 0.000075, -0.2, 300]),
                               self.clock, (214, 40, 40))
        self.defence.observations = []

