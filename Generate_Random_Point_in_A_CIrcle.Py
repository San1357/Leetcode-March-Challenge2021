#Problem : GENERATE RANDOM POINT IN A CIRCLE '''

#CODE :


class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.x_min, self.x_max = x_center - radius, x_center + radius
        self.y_min, self.y_max = y_center - radius, y_center + radius
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center
        

    def randPoint(self) -> List[float]:
         while True:
            x, y = random.uniform(self.x_min, self.x_max), random.uniform(self.y_min, self.y_max)
            if (x - self.x_center)**2 + (y - self.y_center)**2 <= self.radius**2:
                return [x, y]

