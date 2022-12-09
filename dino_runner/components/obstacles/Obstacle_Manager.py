import random
import pygame
from dino_runner.components.obstacles.Bird import Bird
from dino_runner.components.obstacles.Cactus import Cactus
from dino_runner.utils.constants import (LARGE_CACTUS, SMALL_CACTUS, BIRD)

class ObstacleManage():
    def __init__(self):
        self.obstacles = []

    def update(self,game):
        if len(self.obstacles) == 0:
            cactus_size = random.randint(0,1)
            if cactus_size == 0:
                self.large_cactus = Cactus(LARGE_CACTUS)
                self.large_cactus.rect.y = 300
                self.obstacles.append(self.large_cactus)
            elif cactus_size == 1:
                self.obstacles.append(Bird(BIRD))
            else: 
                self.obstacles.append(Cactus(SMALL_CACTUS))
        
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.dino.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(100)
                game.player_heart_manager.reduce_heart()
                
                if game.player_heart_manager.heart_count > 0:
                    self.obstacles.pop()
                    game.dino.has_lives = True
                else:
                    
                    game.dino.has_lives = False
                    game.playing = False
                    break
    
    def draw(self,screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

          