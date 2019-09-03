
class MyClass:
    def __init__(self):
        self.greating = 'Hello my friend....I am a simple class'

    def __str__(self):
        return self.greating

    @property
    def greating_handle(self):
        return self.greating

    @greating_handle.setter
    def greating_handle(self, val):
        print('Thing are changing.....')
        self.greating = val

if __name__ == '__main__':

    c1 = MyClass()

    print(c1)

    c1.greating_handle = 'Hey again, You are curiosity!'

    print(c1)
