import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def euclidean_distance(point1, point2):
    return math.sqrt((point2.x - point1.x)**2 + (point2.y - point1.y)**2)

# Example usage:
point_a = Point(1, 2)
point_b = Point(4, 6)

distance = euclidean_distance(point_a, point_b)
print(f"The Euclidean distance between ({point_a.x}, {point_a.y}) and ({point_b.x}, {point_b.y}) is: {distance}")
