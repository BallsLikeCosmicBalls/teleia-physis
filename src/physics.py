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

    def update(self, dt):
        self.velocity.x += self.acceleration.x * dt
        self.velocity.y += self.acceleration.y * dt

        self.position.x += self.velocity.x * dt
        self.position.y += self.velocity.y * dt

class Spring(PhysicsObject):
    pass

class Rope(PhysicsObject):
    pass

class ConstantMagnet(PhysicsObject):
    pass

class ElectroMagnet(PhysicsObject):
    pass

class Anchor:
    pass


