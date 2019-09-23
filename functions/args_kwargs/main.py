def func1(*args):
    for arg in args:
        print(arg)
    else:
        print('End of the methode.... it is so sad.... :(')

def func2(**kwargs):
    for key, value in kwargs.items():
        print('{} ----> {}'.format(key, value))

    else:
        print('it is done!!!!')

if __name__ == '__main__':
    print('Hello multiple arguments!!!!\n')

    func1('dogy', 'kitty', 'mesaure failure')

    func2(foo='bar', food='bars')
