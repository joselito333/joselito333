import pygame

class Ship:
    """Clase que servira para manejar el barco"""
    def __init__(self, ai_game):
        """inicializa el barco y su posicion inicial"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        
        #carga la imagen del barco y arma su rectangulo
        self.image = pygame.image.load("C:/Users/Jose Jaime/alien_invasion/alien_invasion/images/ship.bmp")
        self.rect = self.image.get_rect()
        
        #inicia cada nuevo barco abajo en el centro de la pantalla
        self.rect.midbottom = self.screen_rect.midbottom
        
        #almacena un Nro Flotante para guardar la posicion horizontal exacta del barco
        self.x = float(self.rect.x)
         
        #flag de movimiento; inicia con un barco que no se esta moviendo
        self.moving_right = False
        self.moving_left = False
        
    def update(self):
        """Actualiza la posicion del barco basado en los flags de movimiento"""
        #Actualiza la coordenada x del barco, no la del rectangulo
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
            
        #Actualiza el Objeto Rectangulo a partir de self.x
        self.rect.x = self.x

        
    def blitme(self):
        #dibuja el barco en su actual posicion
        self.screen.blit(self.image, self.rect)