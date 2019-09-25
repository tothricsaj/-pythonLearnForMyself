class Animal():

    animals_secret = 'We can talk...mostly the ducks....'

    def __init__(self, name):
        self.name = name

    def say_name(self):
        print('Hi, my name is {}!'.format(self.name))



class MeatEater():
    def __init__(self, favorite_food):
        print('One of the MeatEater was created....we are everywhere...')
        self.favorite_food = favorite_food

    def say_favorite_food(self):
        print('My favorite_food is {}'.format(self.favorite_food))


class Dog(Animal, MeatEater):
    def __init__(self, name, dog_type, favorite_food):
        super().__init__(name)
        super().__init__(favorite_food)
        self.dog_type = dog_type

    def say_name(self):
        print('woff, woff I am {}'.format(self.name))

    def say_type(self):
        print('My type is {}'.format(self.dog_type))
        super().say_name()


if __name__ == '__main__':
    print('Hello inheritance!\n')

    dog = Dog('Fluffy', 'terrier', 'cats')

    dog.say_name()
    dog.say_type()

    print(dog.animals_secret)
    
    dog.say_favorite_food()
