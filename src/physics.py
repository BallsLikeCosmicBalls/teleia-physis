class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar):
        return Vector2(self.x * scalar, self.y * scalar)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self


class PhysicsObject:
    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity
        self.acceleration = Vector2(0, 0)

    def update(self, dt, aspect_ratio, radius, decay):
        self.velocity.x += self.acceleration.x * dt
        self.velocity.y += self.acceleration.y * dt

        self.position.x += self.velocity.x * dt
        self.position.y += self.velocity.y * dt

        if self.position.y < -1 + radius:
            self.velocity.y = -self.velocity.y * decay
            self.position.y = -1 + radius

        elif self.position.y > 1 - radius:
            self.velocity.y = -self.velocity.y * decay
            self.position.y = 1 - radius

        if self.position.x < -1 * aspect_ratio + radius:
            self.velocity.x = -self.velocity.x * decay
            self.position.x = -1 * aspect_ratio + radius

        elif self.position.x > 1 * aspect_ratio - radius:
            self.velocity.x = -self.velocity.x * decay
            self.position.x = 1 * aspect_ratio - radius

        if self.position.y <= -1 + radius or self.position.y >= 1 - radius:
            self.velocity.x *= decay

        if 0.01 > self.velocity.x > -0.01:
            self.velocity.x = 0

        if 0.01 > self.velocity.y > -0.01:
            self.velocity.y = 0

class ConstantMagnet(PhysicsObject):
    pass

class ElectroMagnet(PhysicsObject):
    pass

class Anchor:
    pass

class Spring:
    pass

class Rope:
    pass

