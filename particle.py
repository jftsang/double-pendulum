class Particle():
    def __init__(self, mass, position, velocity):
        self.mass = mass
        self.position = position
        self.velocity = velocity

    def apply_force(self, force, dt): #force is a list/array of dimensions, probably given by numpy. 
        ax = force[0] / self.mass
        ay = force[1] / self.mass
        self.velocity[0] += ax * dt
        self.velocity[1] += ay * dt
        self.position[0] += self.velocity[0] * dt
        self.position[1] += self.velocity[1] * dt
    
    def __repr__(self):
        return f"Particle(pos={self.position}, vel={self.velocity})"

