
def convert(s, numRows):
    if numRows == 1 or numRows > len(s):
        return s
    
    list_chars = []
    for _ in range(numRows):
        list_chars.append([])

    i = 0
    step = 1
    rowIdx = 0

    while i < len(s):
        list_chars[rowIdx].append(s[i])
        rowIdx = rowIdx + step

        if rowIdx == numRows:
            step = -step
            rowIdx -=2
        
        if rowIdx == -1:
            step = -step
            rowIdx += 2

        i += 1

    result = ''
    for lst in list_chars:
        result += ''.join(lst)

    return result

print(convert('PAYPALISHIRING', 3))
print(convert('PAYPALISHIRING', 4))