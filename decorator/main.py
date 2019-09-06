def my_decorator(func):
    def wrapper(*args, **kwargs):

        print('Before call')
        result = func(*args, **kwargs)
        print('After call')

        return result

    return wrapper

@my_decorator
def add(a, b):
    'Add two numbers'
    return a + b

def star_decorator(count_of_stars):
    def wrapped_func(func):
        def wrapper(*args, **kwargs):
            print('*' * count_of_stars)
            func(*args, **kwargs)
            print('*' * count_of_stars)
        return wrapper
    return wrapped_func


@star_decorator(40)
def plot_txt(txt):
    print(txt)


if __name__ == '__main__':
    print('hello decorator!!!\n')
    
    print(add(1,3))

    plot_txt('Hello Decorator!!!!')
