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

    currentMax = 0
    currentMaxDown = 0
    currentMaxUp = 0
    currentMaxLeft = 0
    currentMaxRight = 0

    for i in range(1, rows + 1):

        maxBorderDown = 0
        maxBorderUp = 0
        maxBorderLeft = 0
        maxBorderRight = 0
        for j in range(1, columns + 1):
            # Down Border
            if table[i][j] == "#" and table[i + 1][j] != "#":
                maxBorderDown += 1
            if table[i][j] == "#" and table[i + 1][j] == "#":
                maxBorderDown = 0
            if currentMaxDown < maxBorderDown:
                currentMaxDown = maxBorderDown

            # Up Border
            if table[i][j] == "#" and table[i - 1][j] != "#":
                maxBorderUp += 1
            if table[i][j] == "#" and table[i - 1][j] == "#":
                maxBorderUp = 0
            if currentMaxUp < maxBorderUp:
                currentMaxUp = maxBorderUp

            # Left Border
            if table[i][j] == "#" and table[i][j - 1] != "#":
                maxBorderLeft += 1
            if table[i][j] == "#" and table[i][j - 1] == "#":
                maxBorderLeft = 0
            if currentMaxLeft < maxBorderLeft:
                currentMaxLeft = maxBorderLeft

            # Right Border
            if table[i][j] == "#" and table[i][j + 1] != "#":
                maxBorderRight += 1
            if table[i][j] == "#" and table[i][j + 1] == "#":
                maxBorderRight = 0
            if currentMaxRight < maxBorderRight:
                currentMaxRight = maxBorderRight

    currentMax = max(currentMaxDown, currentMaxUp, currentMaxLeft, currentMaxRight)
    print(currentMax)
    testcase -= 1