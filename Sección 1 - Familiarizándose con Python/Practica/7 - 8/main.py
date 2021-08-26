# def multiplyString(s: str, n: int) -> str:
#     """
#     "Multiplies" a string and returns it
 
#         Parameters:
#             s (str): The string that will be multiplied
#             n (int): How many times the string must be multiplied

#         Returns:
#             str: A "multiplied" string
#     """

#     return s * n



# Alternativo con recursión-----------
def multiplyString(s: str, n: int) -> str:
    """
    "Multiplies" a string and returns it
 
        Parameters:
            s (str): The string that will be multiplied
            n (int): How many times the string must be multiplied

        Returns:
            str: A "multiplied" string
    """
    if n <= 0: return ''

    output = s + multiplyString(s, n - 1)
    return output

        


if __name__ == '__main__':
    print(multiplyString('Zehnya', 3))
    print(multiplyString('', 10))
    print(multiplyString('ReNo', 5))
