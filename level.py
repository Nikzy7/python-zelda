import pygame
from settings import *
from tile import Tile
from player import Player

class Level:
    def __init__(self) -> None:
        # get the display surface
        self.display_surface = pygame.display.get_surface()

        #sprite group setup
        self.visible_sprites = YSortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()

        #sprite setup
        self.createMap()

    def createMap(self):
        for rowIndex,row in enumerate(WORLD_MAP):
            for columnIndex,col in enumerate(row):
                x = columnIndex * TILE_SIZE
                y = rowIndex * TILE_SIZE

                if col == 'x':
                    Tile((x,y),[self.visible_sprites,self.obstacle_sprites])
                if col == 'p':
                    self.player = Player((x,y),[self.visible_sprites],self.obstacle_sprites)


    def run(self):
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()

class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        # general setup
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

    def custom_draw(self,player):
        # getting the offset
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        # for sprite in self.sprites():
        for sprite in sorted(self.sprites(),key=lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image,offset_pos) # draw the sprite
