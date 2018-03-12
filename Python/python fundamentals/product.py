##### Product

class Product(object):
    def __init__(self, price, item_name, weight, brand):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = 'for sale'
    def sell(self):
        self.status = 'sold'
        return self
    def add_tax(self, val):
        tax = self.price * val
        self.price += tax
        print 'Price with tax {}'.format(self.price)
        return self
    def bring_back(self, strg):
        if strg =='defective':
            self.status = 'defective'
            self.price = 0
        elif strg == 'like new in box':
            self.status = 'for sale'
        elif strg == 'open box':
            self.status = 'used'
            print '{} - 20%'.format(self.price) 
        return self
    def display_info(self):
        print 'Price: {}\nItem name: {}\nWeight: {}\nBrand: {}\nStatus: {}'.format(self.price, self.item_name, self.weight, self.brand, self.status)
        return self

item1 = Product(5,'cherios', 1, 'lucky charms')

print item1.bring_back('open box').display_info()
        
