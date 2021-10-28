import math

size = int(input("Enter the size of sudoku: "))
print(f"The sudoku grid size is {size} by {size} \n")

sudokuGrid = []

print("Input the elements of the sudoku grid row-wise \n")
for i in range(size):
    rw = list(map(int, input("Enter the numbers in the row and 0 for empty space: ").split()[:size]))
    sudokuGrid.append(rw)

for rw in range(size):
    print(sudokuGrid[rw])

area = int(math.sqrt(size))
print(f"Size of each area is: {area} by {area}")

gridUpdated = True
while (gridUpdated):
    gridUpdated = False

    for target in range(1,size+1):
        row = 0

        while (row < size):

            col = 0

            while (col < size):
                print("\nChecking the following area for target value: ",
                target)
                print("start row: ", row)
                print("end row: ", row + area - 1)
                print("start col: ", col)
                print("end col: ", col + area - 1)
                print()

                #  print(f"Looking for {target}")
                foundTarget = False
                for r in range(row, row + area):
                    for c in range(col, col + area):
                        print(sudokuGrid[r][c])
                        if (sudokuGrid[r][c] == target):
                            foundTarget = True
                            break
                            #  print("target already in area")
                        #  else:
                            #  print(" - Not here")
                print ("The target value ", target, end="")
                if not foundTarget:
                    print(" was not in area")
                    placeTargetAt = []
                    for r in range(row, row+area):
                        for c in range(col, col+area):
                            print(f"Checking row  {r} column {c}")
                            if (sudokuGrid[r][c] == 0):
                                print("Square available")
                                # Get current values for this row
                                currentRowValues = sudokuGrid[r]
                                # and values for the column
                                currentColValues = [item[c] for item in sudokuGrid]
                                print(f"Row contains {currentRowValues}")
                                print(f"Col contains {currentColValues}")
                                if target not in currentRowValues and target not in currentColValues:
                                    print(f"Could place {target} at ({r}, {c})")
                                    placeTargetAt.append([r,c])
                    if (len(placeTargetAt) == 1):
                        print (f"placed {target} at {placeTargetAt[0][0]} x {placeTargetAt[0][1]}")
                        sudokuGrid[placeTargetAt[0][0]][placeTargetAt[0][1]] = target
                        gridUpdated = True

                else:
                    print(" was found in area")
                col += area
            row += area

    for row in range(0,size):
                if 0 in sudokuGrid[row]:
                    for col in range(0,size):
                        if sudokuGrid[row][col] == 0:
                            currentRowValues = sudokuGrid[row]
                            currentColValues = [item[col] for item in sudokuGrid]
                            validChoices = []
                            for n in range(1,size+1):
                                if n not in currentRowValues and n not in currentColValues:
                                    validChoices.append([row, col, n])
                            if len(validChoices) == 1:
                                x, y, n = validChoices[0][0], validChoices[0][1], validChoices[0][2]
                                sudokuGrid[x][y] = n
                                gridUpdated = True


for row in range(size):
    print(sudokuGrid[row])
