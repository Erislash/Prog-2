def sumFirstN(n: int, m: int) -> int:
    """
    Returns the sum of the natural numbers greater than "n" and less than "m" ("n" and "m" are not included in the sum)
 
        Parameters:
            n (int): Lower bound
            m (int): Upper bound

        Returns:
            int: Sum of the natural numbers greater than "n" and less than "m"
    """

    if m <= n + 1: 
        return 0
    else:
        return (m - 1) + sumFirstN(n, m - 1)
        


if __name__ == '__main__':
    print(sumFirstN(2, 4))
