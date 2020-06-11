import pygame
from ray import Ray
from wall import Wall
import numpy as np

def dist(x1, y1, x2, y2):
	return (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)

class Point:
	def __init__(self, pos, n):
		self.x, self.y = pos
		self.rays = []

		for i in range(n):
			self.rays.append(Ray(self.x, self.y, i * 2 * np.pi / n))

	def update(self, pos):
		self.x, self.y = pos
		for ray in self.rays:
			ray.x = self.x
			ray.y = self.y

	def look(self, walls, screen):
		for i in range(len(self.rays)):
			ray = self.rays[i]
			clostest = None
			record = np.Inf

			for wall in walls:
				x1, y1 = ray.cast(wall)
				if x1 == -100 and y1 == -100:
					continue
				d = dist(x1, y1, self.x, self.y)

				if d < record:
					clostest = (x1, y1)
					record = d
			if clostest != None:
				pygame.draw.line(screen, pygame.Color(255, 255, 255), (ray.x, ray.y), clostest)


	def draw(self, screen):
		pygame.draw.circle(screen, pygame.Color(255, 255, 255), (self.x, self.y), 3)