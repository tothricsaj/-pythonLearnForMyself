class Test:

    __my_private = 'I am a private variable!'
    
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __repr__(self):
        return 'This is a prnt object example. The a -> {} and the b -> {}'.format(self.a, self.b)

    def __str__(self):
        return 'This is a prnt object example. The a -> {} and the b -> {}'.format(self.a, self.b)



if __name__ == '__main__':
    print('Hello belloooo!!!\n')
    t = Test(2,3)
    print(t)
    print([t])
