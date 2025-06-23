class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator=numerator
        self.denominator=denominator

    def __str__(self): #Will automatically initialize when object is passed in print
        return "{}/{}".format(self.numerator,self.denominator)
    
    def __add__(self,other):
        temp_num=self.numerator * other.denominator + other.numerator * self.denominator
        temp_den= self.denominator* other.denominator
        return "{}/{}".format(temp_num,temp_den)
    
    def __sub__(self,other):
        temp_num=self.numerator * other.denominator - other.numerator * self.denominator
        temp_den= self.denominator* other.denominator
        return "{}/{}".format(temp_num,temp_den)
    
    def __mul__(self,other):
        temp_num=self.numerator * other.numerator
        temp_den= self.denominator* other.denominator
        return "{}/{}".format(temp_num,temp_den)
    
    def __truediv__(self,other):
        temp_num=self.numerator * other.denominator
        temp_den= self.denominator* other.numerator
        return "{}/{}".format(temp_num,temp_den)

x=Fraction(4,5)
y=Fraction(1,2)
print(x+y)
print(x-y)
print(x*y)
print(x/y)
        