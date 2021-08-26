def sumFirstN(n: int) -> int:
    """
    Reruens the sum of the "n" first natural numbers

        Parameters:
            n (int): How many natural numbers you want to sum 

        Returns:
            int: Sum of the first "n" natural numbers
    """

    if n <= 0: 
        return 0
    else: 
        return n + sumFirstN(n - 1)
