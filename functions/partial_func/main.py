from functools import partial

def f(a,b,c,x):
    return 1000*a + 100*b + 10*c + x

g = partial(f, 3, 4, 1)

if __name__ == '__main__':
    print('Hello partial!\n')
    print(g(5))

