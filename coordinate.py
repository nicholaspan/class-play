class Coordinate(object):
    # Initialize your attributes for Coordinate object
    def __init__(self, x, y):
        self.x = x
        self.y = y 
    # Define the output of print(object)
    def __str__(self):
        human_readable = "<" + str(self.x) + "," + str(self.y)+">"
        return(human_readable)
    # Method: Calculate distance between two Coordinate objects
    def distance(self, other):
        length=((self.x - other.x)**2.0 + (self.y - other.y)**2.0)**(0.5)
        print(length)
        return length