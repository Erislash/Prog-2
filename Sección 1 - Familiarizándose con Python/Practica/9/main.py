def add(n: int, m: int) -> int:
    return n + m

def sub(n: int, m: int) -> int:
    return n - m

def mult(n: int, m: int) -> int:
    return n * m

def div(n: int, m: int) -> int:
    return n / m
        
def operation(None):
    """
    Performs a basic operation based on an user's input
 
        Parameters:
            None

        Returns:
            None
    """


    n = 0
    m = 1
    exit = False

    while (not exit):
        option = input('Enter what operation you want to perform:\n\t- "Suma"\n\t- "Resta"\n\t- "Multiplicacion"\n\t- "Division"\n\t- "Salir"\n--> ')

        if (option.lower() == 'salir'):
            exit = True

        if (not exit):

            if (option.lower() != 'suma' and 
                option.lower() != 'resta' and 
                option.lower() != 'multiplicacion' and 
                option.lower() != 'division'):
                print('Invalid operation')
            else:
                n = int(input("Enter the first number\n\t--> "))
                m = int(input("Enter the second number\n\t--> "))

                if (option.lower() == 'suma'):
                    print(f'{n} + {m} = {add(n, m)}')
                    return add(n, m)

                elif (option.lower() == 'resta'):
                    print(f'{n} - {m} = {sub(n, m)}')
                    return sub(n, m)

                elif (option.lower() == 'multiplicacion'):
                    print(f'{n} x {m} = {mult(n, m)}')
                    return mult(n, m)

                elif (option.lower() == 'division'):
                    print(f'{n} / {m} = {div(n, m)}')
                    return div(n, m)
    


if __name__ == '__main__':
    operation()
