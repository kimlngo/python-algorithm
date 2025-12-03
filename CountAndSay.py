def countAndSay(n: int):
    if n == 1:
        return "1"
    
    return runLengthEncoding(countAndSay(n - 1))

def runLengthEncoding(text: str):
    '''
    convert run length encoding:
    example: "3322251" --> "23321511"
    we replace "33" with "23", replace "222" with "32", replace "5" with "15" and replace "1" with "11". Thus the compressed string becomes "23321511"
    '''

    length = len(text)
    i = 1
    cur = text[0]
    inner_list = [cur]
    grouped_list = []
    result = ''

    while i < length:
        if cur != text[i]:
            grouped_list.append(inner_list)
            inner_list = []
            cur = text[i]
        
        inner_list.append(text[i])
        i += 1

    grouped_list.append(inner_list)

    for lst in grouped_list:
        result += str(len(lst))
        result += lst[0]

    return result

for i in range(1,6):
    print(countAndSay(i))