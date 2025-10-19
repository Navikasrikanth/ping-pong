import pygame
import random
import os

# ball.py
class Ball:
    def __init__(self, x, y, width, height, screen_width, screen_height):
        self.original_x = x
        self.original_y = y
        self.x = x
        self.y = y
        self.width = width   # Make sure this is the bigger width
        self.height = height # Make sure this is the bigger height
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.velocity_x = random.choice([-5, 5])
        self.velocity_y = random.choice([-3, 3])


        # Load sounds
        self.sounds = {
            "paddle": pygame.mixer.Sound(os.path.join("sounds", "paddle_hit.mp3")),
            "wall": pygame.mixer.Sound(os.path.join("sounds", "wall_bounce.mp3")),
            "score": pygame.mixer.Sound(os.path.join("sounds", "score.mp3")),
        }

    def move(self):
        self.x += self.velocity_x
        self.y += self.velocity_y

        # Bounce off top/bottom
        if self.y <= 0 or self.y + self.height >= self.screen_height:
            self.velocity_y *= -1
            self.sounds["wall"].play()  # Play wall bounce sound

    def check_collision(self, player, ai):
        collided = False

        # Player paddle
        if self.rect().colliderect(player.rect()):
            self.x = player.x + player.width
            self.velocity_x *= -1
            collided = True

        # AI paddle
        if self.rect().colliderect(ai.rect()):
            self.x = ai.x - self.width
            self.velocity_x *= -1
            collided = True

        if collided:
            self.sounds["paddle"].play()  # Play paddle hit sound

    def reset(self):
        self.x = self.original_x
        self.y = self.original_y
        self.velocity_x *= -1
        self.velocity_y = random.choice([-3, 3])
        self.sounds["score"].play()  # Play scoring sound

    def rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
