class EllipticCurve:
    def __init__(self, a, b, p):
        self.a = a
        self.b = b
        self.p = p

    def add_points(self, P, Q):
        if P == (0, 0):
            return Q
        if Q == (0, 0):
            return P

        x1, y1 = P
        x2, y2 = Q

        if P != Q:
            slope = (y2 - y1) * pow(x2 - x1, -1, self.p) % self.p
        else:
            slope = (3 * x1 * x1 + self.a) * pow(2 * y1, -1, self.p) % self.p

        x3 = (slope * slope - x1 - x2) % self.p
        y3 = (slope * (x1 - x3) - y1) % self.p

        return (x3, y3)

# Example usage
curve = EllipticCurve(a=2, b=3, p=97)  # Example curve parameters
P = (3, 6)
Q = (10, 7)

R = curve.add_points(P, Q)
print(f"P + Q = {R}")
