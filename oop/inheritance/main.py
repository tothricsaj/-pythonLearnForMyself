class Animal():
    def __init__(self, name):
        self.name = name

    def say_name(self):
        print('Hi, my name is {}!'.format(self.name))

class Dog(Animal):
    def __init__(self, name, dog_type):
        super().__init__(name)
        self.dog_type = dog_type

    def say_name(self):
        print('woff, woff I am {}'.format(self.name))

    def say_type(self):
        print('My type is {}'.format(self.dog_type))
        super().say_name()


if __name__ == '__main__':
    print('Hello inheritance!\n')

    dog = Dog('Fluffy', 'terrier')

    dog.say_name()
    dog.say_type()
