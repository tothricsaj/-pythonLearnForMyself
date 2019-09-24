def add_welcome(func):
    def wrapper(msg):
        return 'Welcome ' + func(msg)

    return wrapper

@add_welcome
def print_msg(msg):
    return msg

if __name__ == '__main__':
    print('Helllo decorator!!!')

    print(print_msg('my friend'))
