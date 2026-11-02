class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map = {')':'(', ']':'[', '}':'{'}

        for char in s:
            if char not in map.keys():
                stack.append(char)  # opening brackets added automatically
            else:
                if stack:
                    top = stack.pop()
                else:
                    top = '!' # empty stack marker
                if map[char] != top:
                    return False

        return not stack    # empty stack indicates all matching pairs
