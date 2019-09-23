def shoot(txt):
    return txt.upper()

yell = shoot

def whisper(txt):
    return txt.lower()

def just_say(func):
    sentence = func('I am saying someone intresting things.....!!!!')
    print(sentence)

def crater_adder(x):
    def adder(y):
        return x + y

    return adder

add_15 = crater_adder(15)

if __name__ == '__main__':
    print('hello first class object!!!\n')

    print(yell('Hey boy! Have you learn Python?'))
    print('\n')

    just_say(shoot)
    print('\n')
    just_say(whisper)
    print('\n')

    print(add_15(3))
