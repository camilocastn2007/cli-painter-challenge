import matplotlib.pyplot
class Point:

    def __init__(self, x: float, y: float):
        self.x: float = x
        self.y: float = y


class Circle:
    def __init__(self,center:Point,radius:float ):
        self.center: Point = center
        self.radius: float = 0,0

    def Area(self) ->float:
        Area = math.pi(self.radius)**2
        return Area

def draw
    circle = plt.Circle((self.center.x, self.center.y), self.radius, color="r")
    plt.gca().add_patch(circle)
    plt.axis("scaled")
    plt.show()