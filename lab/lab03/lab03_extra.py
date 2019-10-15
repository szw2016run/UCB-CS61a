""" Optional problems for Lab 3 """

def is_prime(n):
    """Returns True if n is a prime number and False otherwise.

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    "*** YOUR CODE HERE ***"
    def helper(i):
        if i > n ** 0.5:
            return True
        elif n % i == 0:
            return False
        return helper(i + 1)
    return helper(2)

def gcd(a, b):
    """Returns the greatest common divisor of a and b.
    Should be implemented using recursion.

    >>> gcd(34, 19)
    1
    >>> gcd(39, 91)
    13
    >>> gcd(20, 30)
    10
    >>> gcd(40, 40)
    40
    """
    "*** YOUR CODE HERE ***"
    if a % b == 0:
        return b
    return gcd(b, a % b)

def ten_pairs(n):
    """Return the number of ten-pairs within positive integer n.

    >>> ten_pairs(7823952)
    3
    >>> ten_pairs(55055)
    6
    >>> ten_pairs(9641469)
    6
    """
    "*** YOUR CODE HERE ***"
    # def helper(n, target, count):
    #     if (target == 0):
    #         count += 1
    #     if (target < 0):
    #         return count;
        
    #     for i in range(1,len(str(n))+1):
    #         helper(n // 10**i, target -  (n // 10**(i - 1) % 10), count)

    #     return count


    # return helper(n, 10, 0)
    if n < 10:
        return 0 # base case
    return ten_pairs(n // 10) + count_digit(n // 10, 10 - n % 10) #分解为更小的问题，ten_pairs(n // 10),解决count_digit(n // 10, 10 - n % 10)

def count_digit(n, target):
    if n == 0:
        return 0
    else:
        if (n % 10 == target):
            return count_digit(n // 10, target) + 1
        else:
            return count_digit(n // 10, target)

