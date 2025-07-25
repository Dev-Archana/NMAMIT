rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = []

print("Enter matrix elements row by row:")
for i in range(rows):
    row = []
    for j in range(cols):
        element = int(input(f"Element [{i+1},{j+1}]: "))
        row.append(element)
    matrix.append(row)

print("\nThe matrix is:")
for row in matrix:
    print(" ".join(map(str, row)))
