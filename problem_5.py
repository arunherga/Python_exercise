"""
5. Write a function which takes numbers till user input,
if number is divisible by 3, print "Three"
if number is divisible by 5, print "Five"
if number is divisible by both 5 and 3, print "Three and Five"
else, print the number.


"""

def number_till_user_input():
    num = input("Enter the number:")

    if num != 'q' :
        num = int(num)
        if (num % 5 == 0) and (num % 3 == 0):
            print("Three and Five")
        elif num % 3 == 0:
            print("Three")
        elif num % 5 == 0 :
            print("Five")
        else : print (num)

        number_till_user_input()
    else : return None


if __name__ == '__main__':
    number_till_user_input()  # enter q to end user input 
