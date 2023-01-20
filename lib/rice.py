import pygame
import random
import lib.farm as farm


class rice:  # 파일 따로 빼자,...
    def __init__(self, img, screen, playerTilePos):
        self.tilePos = [32 * playerTilePos[0], 32 * playerTilePos[1]]
        self.growCount = 0
        self.img = img
        self.age = 0
        self.screen = screen

    def draw(self):
        self.screen.blit(self.img, self.tilePos)

    def grow(self):
        self.growCount += random.randint(0, 5)
        if (self.growCount >= 10000) and (self.age == 0):
            print(self.growCount, self.age)
            self.img = pygame.image.load("assets/img/farm_rice_1.png")
            self.age = 1
        if (self.growCount >= 25000) and (self.age == 1):
            self.img = pygame.image.load("assets/img/farm_rice_2.png")
            self.age = 2
