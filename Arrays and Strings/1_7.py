import math

def rotate(m):
    n = len(m)
    print(math.floor(n/2))
    for layer in range (0, math.floor(n/2)):
        for j in range (layer, n-layer):
            temp = m[layer][j]
            m[layer][j] = m[n-j-1][layer]
            m[n-j-1][layer] = m[n-layer-1][n-j+layer-1]
            m[n-layer-1][n-j+layer-1] = m[j][n-layer-1]
            m[n-layer-1][j] = temp

            #m[layer][j] = m[j][n-layer-1]
            #m[j][n-layer-1] = m[n-layer-1][n-j-1]
            #m[n-layer-1][n-j-1] = m[n-j-1][layer]
            #m[n-j-1][layer] = temp

            #temp = m[layer][layer]
            #m[layer][layer] = m[layer][n-layer-1]
            #m[layer][n-layer-1] = m[n-layer-1][n-layer-1]
            #m[n-layer-1][n-layer-1] = m[n-layer-1][layer]
            #m[n-layer-1][layer] = temp
    return(m)




if __name__ == "__main__":
    n = 6
    w, h = n, n;
    matrix = [[0 for x in range(w)] for y in range(h)]
    print(len(matrix))
    m = [[1, 1, 1, 1, 1, 1],
    [2,2,2,2,2,2],
    [3,3,3,3,3,3],
    [4,4,4,4,4,4],
    [5,5,5,5,5,5],
    [6,6,6,6,6,6]]
    k = [[1 , 1, 1],
    [2, 2, 2],
    [3, 3, 3]]
    print(rotate(m))
