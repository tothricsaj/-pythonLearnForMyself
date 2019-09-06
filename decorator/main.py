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


if __name__ == '__main__':
    print('hello decorator!!!\n')
    
    print(add(1,3))
