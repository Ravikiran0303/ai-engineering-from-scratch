class Vector:

    def __init__(self, components):
        self.components = components
        self.dim = len(self.components)

    def __add__(self, other):
        return Vector([a+b for a, b in zip(self.components, other.components)])

    def __sub__(self, other):
        return Vector([a-b for a, b in zip(self.components, other.components)])

    def __mul__(self, scalar):
        return Vector([x*scalar for x in self.components])

    def dot(self, other):
        return sum(a*b for a, b in zip(self.components, other.components))
    
    def magnitude(self):
        return sum(x**2 for x in self.components) ** 0.5

    def normalize(self):
        mag = self.magnitude()
        return Vector([x/mag for x in self.components])
    
    def cosine_similarity(self, other):
        return self.dot(other)/(self.magnitude() * other.magnitude())

    def angle_between(self, other):
        import math
        cos_theta = self.cosine_similarity(other)
        cos_theta = max(-1.0, min(1.0, cos_theta))
        return math.degrees(math.acos(cos_theta))

    def project_onto(self, other):
        scalar = self.dot(other)/ other.dot(other)
        return Vector([scalar * x for x in other.components])

    def __repr__(self):
        return f"Vector({self.components})"


if __name__ == "__main__":
    v1 = Vector([1, 2, 3])
    v2 = Vector([4, 5, 6])

    print("v1 + v2 =", v1.__add__(v2))
    print("v1 - v2 =", v1.__sub__(v2))
    print("v1 * 2 =", v1.__mul__(2))
    print("Dot product:", v1.dot(v2))
    print("Magnitude of v1:", v1.magnitude())
    print("Normalized v1:", v1.normalize())
    print("Cosine similarity:", v1.cosine_similarity(v2))
    print("Angle between v1 and v2:", v1.angle_between(v2))
    print("Projection of v1 onto v2:", v1.project_onto(v2))
    print("Projection of v2 onto v1:", v2.__repr__())
