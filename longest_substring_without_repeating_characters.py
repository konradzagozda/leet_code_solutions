# brute force approach
def lengthOfLongestSubstring(s: str) -> int:
    chars = []
    maximum = 0
    for i in range(len(s)): # iter over every letter # todo could optimize at the end of string
        for j in range(i, len(s)):
            if s[j] not in chars:
                chars.append(s[j])
                if len(chars) > maximum:
                    maximum = len(chars)
            else:
                chars.clear()
                break
    return maximum

# sliding window approach
def lengthOfLongestSubstringSlidingWindow(s: str) -> int:
    chars = []
    maximum = 0
    for char in s:
        while char in chars:
            chars.pop(0)
        else:
            chars.append(char)
            if maximum < len(chars):
                maximum = len(chars)
    return maximum


print(lengthOfLongestSubstring("dvdf"))
