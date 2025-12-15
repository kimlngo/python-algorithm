def longestSubStringNoDup(s: str) -> int:
    length = len(s)
    if length < 2:
        return len(s)
    
    seen = []
    maxLen = -1

    for i in range(0, length):
        for j in range(i, length):
            char = s[j]

            if char not in seen:
                seen.append(char)
            else:
                maxLen = max(maxLen, len(seen))
                seen = []
                break
    
    return maxLen

print(longestSubStringNoDup("abcadef"))