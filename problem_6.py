"""
6. Write a function which will check if a given number is outside a given range.
Ex:is_out_of_range(number, start, end) will return True if number is out
of range, False if number is withiin range.
Test:
is_out_of_range(12, 0, 36) returns False
is_out_of_range(12, 12, 36) returns False
is_out_of_range(120, 0, 36) returns True


"""

def is_our_of_range(number, start, end):
    if (number < start) or (number > end):
        return True
    else: return False

if __name__ == '__main__':
    print(is_our_of_range(12, 0, 36))
    print(is_our_of_range(12, 12, 36))
    print(is_our_of_range(120, 0, 36))
