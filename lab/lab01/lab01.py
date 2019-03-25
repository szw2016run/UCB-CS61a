"""Lab 1: Expressions and Control Structures"""

# Coding Practice

def repeated(f, n, x):
    """Returns the result of composing f n times on x.

    >>> def square(x):
    ...     return x * x
    ...
    >>> repeated(square, 2, 3)  # square(square(3)), or 3 ** 4
    81
    >>> repeated(square, 1, 4)  # square(4)
    16
    >>> repeated(square, 6, 2)  # big number
    18446744073709551616
    >>> def opposite(b):
    ...     return not b
    ...
    >>> repeated(opposite, 4, True)
    True
    >>> repeated(opposite, 5, True)
    False
    >>> repeated(opposite, 631, 1)
    False
    >>> repeated(opposite, 3, 0)
    True
    """
    "*** YOUR CODE HERE ***"
    i = 1
    res = f(x)
    while(i!=n):
        res = f(res)
        i += 1
    return res




def sum_digits(n):
    """Sum all the digits of n.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    """
    "*** YOUR CODE HERE ***"
    total = 0
    while(n):
        total,n = total + n%10,n//10
    return total


def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    # count = 0
    # while n:
    #     if count == 1:
    #         if n % 10 == 8:
    #             return True
    #         count = 0
    #     a = n%10
    #     if a == 8:
    #         count += 1
    #     n = n//10
    # return False
    """
    prev_eight = False
    while n > 0:
        last_digit = n % 10
        if last_digit == 8 and prev_eight:
            return True
        elif last_digit == 8:
            prev_eight = True
        else:
            prev_eight == False
        n = n//10
    return False
    """
    while(n != 0):
    	last, n = n % 10 , n//10
    	if(last == 8):
    		if(n % 10 == 8):
    			return True
    return False

def keep_ints(cond,n):
    """Print out all integers 1..i..n where cond(i) is true

    >>>def is_even(x):
    ...    # Even numbers have remainder 0 when divided by 2.
    ...    return x % 2 == 0
    >>>keep_ints(is_deven,5)
    2
    4
    """
    for i in range(1,n+1):
        if cond(i):
            print(i)


def keep_ints(n):
    def inner(f):
        for i in range(1,n+1):
            if(f(i)):
                print(i)
    return inner
    