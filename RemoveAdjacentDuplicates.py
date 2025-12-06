def removeDuplicates(s: str) -> str:
    if len(s) == 1:
        return s
    
    stack = []
    stack.append(s[0])

    for i in range(1, len(s)):
        c = s[i]
        if len(stack) == 0:
            stack.append(c)
            continue

        pop = stack.pop()

        if(pop != c):
            stack.append(pop)
            stack.append(c)
    

    return "".join(stack)


print(removeDuplicates('abbaca'))
print(removeDuplicates('azxxzy'))
print(removeDuplicates('aaa'))