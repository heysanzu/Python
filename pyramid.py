def printPyramid(rows):
    for i in range(1, rows + 1):
        # Print spaces
        spaces = rows - i
        print(' ' * spaces, end='')
        
        # Print stars
        stars = 2 * i - 1
        print('*' * stars)

rows = int(input("Enter number of rows: "))
printPyramid(rows)