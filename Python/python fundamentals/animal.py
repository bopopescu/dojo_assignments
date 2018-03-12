###### Animals

class Animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health
    def walk(self):
        self.health -= 1
        return self
    def run(self):
        self.health -= 5
        return self
    def display_health(self):
        print self.health
        return self
class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name, 150)
    def pet(self):
        self.health += 5
        return self
class Dragon(Animal):
    def __init__(self, name):
        super(Dragon, self).__init__(name, 170)
    def fly(self):
        self.health -= 10
        return self
    def display_health(self):
        super(Dragon, self).display_health()
        print 'I am a Dragon'
        return self

cat = Animal('cat', 20)
cat.display_health().walk().walk().walk().run().run().display_health()

dog1 = Dog('rover')
dog1.display_health().run().run().pet().display_health()

dragon = Dragon('drag')
dragon.display_health()

fish = Animal('nemo', 50)
fish.display_health()
