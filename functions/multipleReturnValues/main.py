if __name__ == "__main__":
    print('hello multiple return values :S\n')

    ############################################
    # using object ---->

    class Test:
        def __init__(self):
            self.str = "This is a string value"
            self.integer = 23

    def func():
        return Test()

    f = func()
    print(f.str)
    print(f.integer)

    print('\n')

    ############################################
    # using tuples ------->

    def tuple_func():
        return 'Tuple string', 42

    str, integer = tuple_func()
    print(str)
    print(integer)

    print('\n')

    ############################################
    # using dictionary ----------->

    def dic_func():
        d = dict()
        d['str'] = 'Dictionary String'
        d['x'] = 2323

        return d

    d = dic_func()
    print(d)
    print(d["str"])
    print(d["x"])

    print('\n')

    ############################################


