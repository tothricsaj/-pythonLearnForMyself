double = lambda x : 2*x

my_list = [1, 2, 5, 3, 22, 11, 30, 48]

if __name__ == '__main__':
    print('Hello lambda!!!!!!!!\n')
    print(double(3))

    new_list = list(
            filter(
                lambda x: (x%2==0), 
                my_list
            )
        )

    print(new_list)
