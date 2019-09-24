def add_welcome(func):
    def wrapper(msg):
        return 'Welcome ' + func(msg)

    return wrapper

def attach_data(data):
    def wrapper(func):
        func.data = data
        return func

    return wrapper

@add_welcome
def print_msg(msg):
    return msg

@attach_data('Little kitty')
def add(x, y):
    return x + y

if __name__ == '__main__':
    print('Helllo decorator!!!')

    print(print_msg('my friend'))

    print(add(4,3))
    print(add.data)

