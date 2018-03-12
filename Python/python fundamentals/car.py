#### Car

class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage 
        if self.price > 10000:
            self.tax = '15%'
        else:
            self.tax = '12%'
        self.display_all()
    def display_all(self):
        print 'Price: {}'.format(self.price)
        print 'Speed: {}'.format(self.speed)
        print 'Fuel: {}'.format(self.fuel)
        print 'Mileage: {}'.format(self.mileage)
        print 'Tax: {}'.format(self.tax)
        return self

car1 = Car(2000, '35mph', 'Half Full', '35mpg')
car2 = Car(5000, '40mph', 'Full', '30mpg')
car3 = Car(12000, '78mph', 'Half Full', '20mpg')
car4 = Car(7000, '20mph', 'Empty', '15mpg')
car5 = Car(20000, '96mph', 'Full', '50mpg')
car6 = Car(30000, '10mph', 'Half Full', '11mpg')

# print car1.display_all()
# print car2
# print car3
# print car4
# print car5
# print car6



        