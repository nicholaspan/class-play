class Fraction(object):
# Defining Fraction object class, playing with special operators
# i.e. __str__, __add__, __sub__, __float__...
    """
    A number represented as a fraction
    """
    def __init__(self, num, denom):
        self.num = num
        self.denom = denom
    def __str__(self):
        return(str(self.num)+"/"+str(self.denom))
    def __add__(self, other):
        top = self.num * other.denom + self.denom * other.num
        bottom = self.denom * other.denom
        return Fraction(top, bottom)
    def __sub__(self,other):
        top = self.num * other.denom + self.denom * other.num
        bottom = self.denom * other.denom
        return Fraction(top, bottom)
    def __float__(self):
        return self.num / self.denom
    def inverse(self):
        return Fraction(self.denom, self.num)