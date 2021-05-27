testcase = int(input())
while testcase:
    rows, columns = map(int, input().split(" "))
    table = [[0 for j in range(columns + 2)] for i in range(rows + 2)]

    for row in range(1, rows + 1):
        col_list = list(input())
        col_list_ind = 0
        for col in range(1, columns + 1):
            table[row][col] = col_list[col_list_ind]
            col_list_ind += 1
    print(table)
    currentMax = 0
    # Down Border
    for i in range(1, rows + 1):
        maxBorder = 0
        for j in range(1, columns + 1):
            if table[i][j] == "#" and table[i + 1][j] != "#":
                maxBorder += 1
            if table[i][j] == "#" and table[i + 1][j] == "#":
                maxBorder = 0
            if currentMax < maxBorder:
                currentMax = maxBorder

    # Up Border
    for i in range(1, rows + 1):
        maxBorder = 0
        for j in range(1, columns + 1):
            if table[i][j] == "#" and table[i - 1][j] != "#":
                maxBorder += 1
            if table[i][j] == "#" and table[i - 1][j] == "#":
                maxBorder = 0
            if currentMax < maxBorder:
                currentMax = maxBorder

    # Left Border
    for i in range(1, rows + 1):
        maxBorder = 0
        for j in range(1, columns + 1):
            if table[i][j] == "#" and table[i][j - 1] != "#":
                maxBorder += 1
            if table[i][j] == "#" and table[i][j - 1] == "#":
                maxBorder = 0
            if currentMax < maxBorder:
                currentMax = maxBorder
    # Right Border
    for i in range(1, rows + 1):
        maxBorder = 0
        for j in range(1, columns + 1):
            if table[i][j] == "#" and table[i][j + 1] != "#":
                maxBorder += 1
            if table[i][j] == "#" and table[i][j + 1] == "#":
                maxBorder = 0
            if currentMax < maxBorder:
                currentMax = maxBorder
    print(currentMax)
    testcase -= 1