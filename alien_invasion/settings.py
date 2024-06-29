class Settings:
    """Clase para almacenar los settings de Invasion Alienigena"""
    
    def __init__(self):
        """inicializacion de los settings"""
        #Screen settings
        self.screen_width = 1000
        self.screen_height = 500
        self.bg_color = (230, 230, 230)
        
        #Ship settings
        self.ship_speed = 3.5
        
        #Bullet settings
        self.bullet_speed = 5.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (250, 0, 0)
        self.bullets_allowed = 4
        
        