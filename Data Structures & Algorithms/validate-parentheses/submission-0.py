class Solution:
    def isValid(self, s: str) -> bool:
        # transferred from leetcode
        stack = []
        map = {')':'(', '}':'{', ']':'['}

        for char in s:
            if char not in map.keys():
                stack.append(char) # only adding opening brackets
            else:
                if stack:
                    top = stack.pop()
                else:
                    top = '#'
                # if the most recent open bracket does not match the current closing bracket
                if (map[char] != top): 
                    return False
        
        return not stack # true if empty