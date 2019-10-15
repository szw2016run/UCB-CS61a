"""Optional questions for Lab 1"""

# While Loops

def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 0)
    1
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    """
    "*** YOUR CODE HERE ***"
    total = 1;
    while k > 0:
        total *= n
        # n--
        # k--没有这种形式
        n -= 1
        k -= 1
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
    # 向下取整java是/ python 是//
    while(n != 0):
        if (n % 10 == 8):
            if n // 10 % 10 == 8:
                return True
            n //= 100
        n //= 10
    return False
    
#官网答案
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






