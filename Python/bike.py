##### Bike

class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    def displayInfo(self):
        print self.price, self.max_speed, self.miles
        return self
    def ride(self):
        print "Riding"
        self.miles += 10
        return self
    def reverse(self):
        print "Reversing"
        self.miles -= 5
        return self


bike1 = Bike('$150', '20mph')
bike2 = Bike('$200', '30mph')
bike3 = Bike('$250', '40mph')

print bike1.ride().ride().ride().reverse().displayInfo()
print bike2.ride().ride().reverse().reverse().displayInfo()
print bike3.reverse().reverse().reverse().displayInfo()