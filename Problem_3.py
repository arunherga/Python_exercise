"""
3. Modify print_symbol function to not print anything greater than 1 character
in length.
Ex: print_symbol(11, 'aa') will not work.

"""



def print_symbol( size, symbol):
    if len(symbol) == 1:
        for i in range(size, 0, -1):
            print(symbol*i, end = '\n')


if __name__ == '__main__':
    print_symbol(11,'**')  # no output as it has more than 1 character