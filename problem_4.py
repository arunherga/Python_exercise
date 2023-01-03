"""
Write a function which will check if a given number is within a given range.
Ex: is_in_range(number, start, end) will return True if number is in range,
False if number is not in range.
Test:
is_in_range(12, 0, 36) returns True
is_in_range(12, 12, 36) returns True
is_in_range(120, 0, 36) returns False
"""

def is_in_range(number,start,end):
    if (number >= start) and (number <= end):
        return True
    else: return False


if __name__ == '__main__' :
    print(is_in_range(12, 0, 36))
    print(is_in_range(12, 12, 36))
    print(is_in_range(120, 0, 36))
