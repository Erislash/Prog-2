def domino(n):
    for i in range(n):
        for j in range(i, n):
            print(f'| {i} || {j} |')

domino(6)