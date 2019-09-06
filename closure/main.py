def add_number(num):
    def adder(number):
        'adder is a closure'
        return num + number
    return adder


if __name__ == '__main__':

    a_10 = add_number(10)
    print(a_10(21))
