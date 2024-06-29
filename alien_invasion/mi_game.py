import sys
import pygame

class Game:
  """Pgma ejemplo del libro solo abre una pantalla y la pinta de azul"""
  def __init__(self):
    pygame.init()
    self.clock = pygame.time.Clock()
    self.screen = pygame.display.set_mode((300, 100))
    pygame.display.set_caption("Mi primera pantalla")
    self.bg_color = (0, 100, 100)


  def run_game(self):
    while True:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          sys.exit()
      self.screen.fill(self.bg_color)
      pygame.display.flip()
      self.clock.tick(60)

if __name__ == '__main__':
  mi_game = Game()
  mi_game.run_game() 