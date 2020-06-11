import pygame
import sys
from wall import Wall
from point import Point

pygame.init()

width, height = 500, 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("RAYCAST 2D")

clock = pygame.time.Clock()


walls = [Wall(200, 200, 100, 300), Wall(400, 100, 200, 300), Wall(0, 0, 0, height), Wall(0, height, width, height), Wall(0, 0, width, 0), Wall(width, 0, width, height)]
p = Point(pygame.mouse.get_pos(), 300)

def main():
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
		
		screen.fill(pygame.Color(0, 0, 0))

		for wall in walls:
			wall.draw(screen)

		p.update(pygame.mouse.get_pos())
		p.draw(screen)
		p.look(walls, screen)
		pygame.display.update()
		clock.tick(30)

		


main()