import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """ Clase para manejar las balas disparadas desde el barco"""
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color
        
        #Cree un rect bala en (0,0) y luego setee la posicion correcta
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
            self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop
        
        #Almacene la posicion de la bala como un nro float
        self.y = float(self.rect.y)
        
    def update(self):
        """Mueve la bala a la parte de arriba del screen"""
        # Actualiza la posicion exacta de la bala
        self.y -= self.settings.bullet_speed
        # Actualiza la posicion del rectangulo
        self.rect.y = self.y
        
    def draw_bullet(self):
        """ Dibuja la bala en el screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
        