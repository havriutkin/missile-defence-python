import pygame
import numpy as np

from EventManager import EventManager
from Missile import Missile
from Settings import Settings


class DefenceSystem:
    def __init__(self, settings: Settings, clock: pygame.time.Clock):
        self.settings = settings
        self.clock = clock

        # Position of system
        self.x = settings.screen_width / 2
        self.y = settings.screen_height - 20
        self.width = 40
        self.height = 40

        # List of launched missiles
        self.missiles = []

        # List of observations list[tuple[t, x, y]]
        self.observations = []

    def update(self):
        for missile in self.missiles:
            missile.update()
            if missile.out_of_screen():
                self.missiles.remove(missile)

    def render(self, screen: pygame.Surface):
        pygame.draw.rect(screen, (252, 191, 73), (self.x - self.width / 2, self.y - self.height / 2,
                                                  self.width, self.height))

        for missile in self.missiles:
            missile.render(screen)

    def add_observation(self, t, x, y):
        self.observations.append((t, x, y))

    def launch_missile(self):
        """Approximate trajectory and launch missile"""
        # Approximate enemy missile path
        traj_x, traj_y = self.approximate()
        t_last = self.observations[-1][0]  # Time of last observation

        # Approximate position of enemy missile in 2 seconds
        x_next = traj_x[0] * (t_last + 2000) ** 3 + traj_x[1] * (t_last + 2000) ** 2 + traj_x[2] * (t_last + 2000) + \
                 traj_x[3]
        y_next = traj_y[0] * (t_last + 2000) ** 3 + traj_y[1] * (t_last + 2000) ** 2 + traj_y[2] * (t_last + 2000) + \
                 traj_y[3]

        # Find linear trajectory for defence missile
        traj_x = [0, 0, (x_next - self.x) / 2000, self.x]
        traj_y = [0, 0, (y_next - self.y) / 2000, self.y]

        # Launch missile
        self.missiles.append(Missile(self.settings, (traj_x, traj_y), self.clock, (0, 255, 0), ttl=2000))

    def approximate(self):
        # Get data from observations
        t_values = [triple[0] for triple in self.observations]
        x_values = [triple[1] for triple in self.observations]
        y_values = [triple[2] for triple in self.observations]

        # Convert to numpy arrays
        t = np.array(t_values)
        x = np.array(x_values)
        y = np.array(y_values)

        # Use linear regression to approximate trajectories
        t = np.vander(t, 4, increasing=True)  # construct vander matrix
        t = np.linalg.pinv(t)  # find pseudo inverse
        trajectory_x = np.matmul(t, x).tolist()[::-1]
        trajectory_y = np.matmul(t, y).tolist()[::-1]

        return trajectory_x, trajectory_y
