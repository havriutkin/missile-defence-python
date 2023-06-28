import pygame

from Settings import Settings


class Missile:
    def __init__(self, settings: Settings, trajectory: tuple[list[float], list[float]], clock: pygame.time.Clock, color, ttl=-1.0):
        self.settings = settings
        self.clock = clock

        # Set up position functions (list of coefficients)
        self.x_t = trajectory[0]
        self.y_t = trajectory[1]

        # Current pose
        self.t_cur = 0
        self.x, self.y = self.get_position(self.t_cur)

        self.is_blown_up = False    # True if blown up, false otherwise
        self.ttl = ttl              # Time to live
        self.color = color

    def get_position(self, t: float):
        """Returns current position by given time"""
        x_pos = self.x_t[0] * t ** 3 + self.x_t[1] * t ** 2 + self.x_t[2] * t + self.x_t[3]
        y_pos = self.y_t[0] * t ** 3 + self.y_t[1] * t ** 2 + self.y_t[2] * t + self.y_t[3]

        return x_pos, y_pos

    def update(self):
        self.t_cur += self.clock.get_time()  # Add time passed from last frame

        # Calculate new position
        self.x, self.y = self.get_position(self.t_cur)

        # Check if missile need to be exploded
        if self.ttl != -1 and self.t_cur >= self.ttl:
            self.is_blown_up = True
            self.color = (255, 0, 0)

    def render(self, screen: pygame.Surface):
        pygame.draw.circle(screen, self.color, (self.x, self.y), 5)

    def out_of_screen(self):
        """Returns true if point is out of screen, false - otherwise"""
        if self.x < 0:
            return True

        if self.x > self.settings.screen_width:
            return True

        if self.y < 0:
            return True

        if self.y > self.settings.screen_height:
            return True

        return False
