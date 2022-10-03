import math


class Point:
    def __init__(self, x=0.0, y=0.0):
        #
        # Write code here
        #
        self.__x=x
        self.__y=y
        

    def getx(self):
        #
        # Write code here
        #
        return self.__x
        
        

    def gety(self):
        #
        # Write code here
        #
        return self.__y

    def distance_from_xy(self, x, y):
        #
        # Write code here
        #
        return math.hypot(x-self.getx(),y-self.gety())
        
    def distance_from_point(self, point):
        #
        # Write code here
        #
        return math.hypot(point.getx()-self.getx(),point.gety()-self.gety())
        
class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        #
        # Write code here
        #
        self.__ver1=vertice1
        self.__ver2=vertice2
        self.__ver3=vertice3

    def perimeter(self):
        #
        # Write code here
        #
        return self.__ver1.distance_from_point(self.__ver2)+self.__ver2.distance_from_point(self.__ver3)+self.__ver3.distance_from_point(self.__ver1)


triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())
