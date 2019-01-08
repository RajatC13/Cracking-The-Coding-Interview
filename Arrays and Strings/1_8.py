
def nullify(m):
    row = [None] *len(m)
    col = [None] *len(m[0])
    for i in range(0, len(m)):
        for j in range(0, len(m[0])):
            if m[i][j] == 0:
                row[i] = True
                col[j] = True

    print(row)
    print(col)


    for i in range(0, len(row)):
        if row[i]:
            for j in range(0,len(m[0])):
                m[i][j] = 0

    for i in range(0, len(col)):
        if col[i]:
            for j in range(0,len(m)):
                m[j][i] = 0
    return(m)




if __name__ == "__main__":
    n = 6
    w, h = n, n;
    matrix = [[0 for x in range(w)] for y in range(h)]
    print(len(matrix))
    m = [[1, 1, 1, 1, 1, 1],
    [2,2,2,2,2,2],
    [3,3,3,3,3,3],
    [4,4,0,4,4,4],
    [5,5,5,5,5,5],
    [6,6,6,6,6,6]]
    k = [[1 , 1, 1],
    [2, 2, 2],
    [3, 3, 3]]
    print(nullify(m))
