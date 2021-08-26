def printEvenNaturals(n: int, m: int) -> None:
    """
    Prints the "n" first even natural numbers, starting from "m"

        Parameters:
            n (int): How many numbers will be printed
            m (int): From which number will start.

        Returns:
            None
    """

    if m <= 0: return
    else:
        if (n % 2 == 0):
            print(n)
            return printEvenNaturals(n + 2, m - 1)
        return printEvenNaturals(n + 1, m)
        


if __name__ == '__main__':
    printEvenNaturals(0, 25)
    print('==========================')
    printEvenNaturals(10, 2) # 10, 12
    print('==========================')
    printEvenNaturals(25, 2) # 26, 28
    print('==========================')
    printEvenNaturals(100, 1) # 100
    print('==========================')
    printEvenNaturals(101, 100) # {x / x es natural, par y 101 < x <= 300}
