def gen_func():
    print('Generating')
    yield 'a'
    yield 'b'
    yield 'c'

if __name__ == '__main__':
    gen_val = gen_func()
    print(next(gen_val))
    print(next(gen_val))
    print(next(gen_val))
    print(next(gen_val))
