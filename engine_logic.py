import pygame as pg
import random

class PhysicsObject:
    def __init__(self,velocity,position,radius,mass,screen):
        self.velocity = velocity
        self.position = position
        self.radius = radius
        self.mass = mass
        self.screen = screen
        self.width = screen.get_width()
        self.height = screen.get_height()

    def draw(self):
        pg.draw.circle(self.screen, (255, 255, 255), self.position, self.radius)

    def update(self):
        if (self.position.x - self.radius <= 0) or (self.position.x + self.radius >= self.width):
            self.velocity.x *= -1

        if (self.position.y  - self.radius <= 0) or (self.position.y + self.radius >= self.height):
            self.velocity.y *= -1

        self.position += self.velocity

    def collide(self,ball):
        normal = ball.position - self.position
        if normal == pg.Vector2(0,0):
            normal.x += 1
        normal = pg.Vector2(normal).normalize()
        relative_velocity = self.velocity - ball.velocity
        relative_velocity = relative_velocity.x * normal.x + relative_velocity.y * normal.y
        if relative_velocity > 0:
            impulse = -(1+1)*relative_velocity/(1/self.mass + 1/ball.mass)
            self.velocity += impulse/self.mass * normal
            ball.velocity -= impulse/ball.mass * normal

class PhysicsWorld:
    def __init__(self,screen):
        self.particles = list()
        self.screen = screen
        self.screen_width = screen.get_width()
        self.screen_height = screen.get_height()

    def add_object(self,amount):
        for i in range(0, amount + 1):
            radius = random.uniform(5, 10)
            particle = PhysicsObject(pg.Vector2(random.uniform(-10, 10), random.uniform(-10, 10)),
                                 pg.Vector2(random.uniform(0, self.screen_width), random.uniform(0, self.screen_height)),
                                 radius, radius * 1.5, self.screen)

            self.particles.append(particle)

    def update(self):
        for particle in self.particles:
            particle.update()

        for particle in range(len(self.particles)):
            for i in range(particle + 1,len(self.particles)):
                if self.particles[particle].radius + self.particles[i].radius >= self.particles[particle].position.distance_to(self.particles[i].position):
                    self.particles[particle].collide(self.particles[i])

        for particle in self.particles:
            particle.draw()