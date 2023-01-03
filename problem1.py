"""
1. Write a function to print symbols in reverse fashion.
Ex: print_symbol(11, '*')
***********
**********
*********
********
*******
******
*****
****
***
**
*


"""



def print_symbol(size,symbol):
    for i in range(size,0,-1):
        print( symbol * i, end = '\n')



if __name__ =='__main__':
    print_symbol( 11, '*')
