def func1(*args):
    for arg in args:
        print(arg)
    else:
        print('End of the methode.... it is so sad.... :(')

if __name__ == '__main__':
    print('Hello multiple arguments!!!!\n')

    func1('dogy', 'kitty', 'mesaure failure')
