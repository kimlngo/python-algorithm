def rotateImage(matrix):
    n = len(matrix)
    if n == 1:
        return
    
    flipVertical(matrix)
    tmp = None

    for row in range(0, n - 1):
        col = 0

        while col < n - 1 - row:
            tmp = matrix[row][col]
            matrix[row][col] = matrix[n - 1 - col][n - 1 - row]
            matrix[n - 1 - col][n - 1 - row] = tmp

            col += 1

def flipVertical(matrix):
    for row in matrix:
        reverseArr(row)

def reverseArr(arr):
    arr.reverse()

matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
rotateImage(matrix)
print(matrix)
