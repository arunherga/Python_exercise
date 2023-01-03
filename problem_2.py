"""
2. Modify print_symbol function to not print anything if symbol is "-".

"""



def print_symbol( size, symbol):
    if symbol != '-':
        for i in range(size,0,-1):
            print(symbol*i,end = '\n')
    else :
        return None
    

if __name__ == '__main__':
    print_symbol(11,'-')  # no output as the charter input is '-'