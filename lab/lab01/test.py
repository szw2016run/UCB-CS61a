def double_eights(n):
    """ Return true if n has two eights in a row.
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
    >>> double_eights(808080)
    False
    """

    prev_eight = False
    while n > 0:
        last_digit = n % 10
        if last_digit == 8 and prev_eight:
            return True
        elif last_digit == 8:
            prev_eight = True
        else:
            prev_eight = False
        n //= 10
    return False
def falling(n, k):
    """Computer the falling factorial of n to depth k.

    >>> falling(6, 3) #6 * 5 * 4
    120
    >>> falling(4, 3) # 4 * 3 * 2
    24
    >>> falling(4, 0)
    1
    >>> falling(4, 1) # 4
    4
    """

    total, stop = 1, n - k
    while n > stop:
        total, n = total * n, n - 1
    return total