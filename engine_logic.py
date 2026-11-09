import pygame as pg

class PhysicsObject:
    def __init__(self,velocity,position,radius,mass,screen):
        self.velocity = velocity
        self.position = position
        self.radius = radius
        self.mass = mass
        self.screen = screen

    def draw(self):
        pg.draw.circle(self.screen, (255, 255, 255), self.position, self.radius)

    def update(self):
        if self.position.x - self.radius <= 0:
            self.velocity.x *= -1
        if self.position.x + self.radius >= self.screen.get_width():
            self.velocity.x *= -1

        if self.position.y  - self.radius <= 0:
            self.velocity.y *= -1
        if self.position.y + self.radius >= self.screen.get_height():
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
    def __init__(self):
        self.particles = list()

    def add_object(self,particle):
        self.particles.append(particle)

    def update(self):
        for particle in range(len(self.particles)):
            self.particles[particle].update()

        for particle in range(len(self.particles)):
            for i in range(particle + 1,len(self.particles)):
                if self.particles[particle].radius + self.particles[i].radius >= self.particles[particle].position.distance_to(self.particles[i].position):
                    self.particles[particle].collide(self.particles[i])

        for particle in range(len(self.particles)):
            self.particles[particle].draw()