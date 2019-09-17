class Animal():
    def intro(self):
        print('This is a animal\n')

    def say_hello(self):
        print('It is basic animal....no type')

class Dog(Animal):
    def say_hello(self):
        print('Wooff, woof wooooooooooooooooooooouuuuuuuuuuuuuufffff')

    def type(self):
        print('It is a dog')

class Cat(Animal):
    
    def say_hello(self):
        print('Meow....meow')


    def type(self):
        print('It is a cat')


if __name__ == '__main__':
    print('Hello polymorphism!\n')

    dog = Dog()
    cat = Cat()

    for animal in (dog, cat):
        animal.say_hello()

