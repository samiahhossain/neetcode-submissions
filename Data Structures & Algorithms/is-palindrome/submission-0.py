class Solution:
    def isPalindrome(self, s: str) -> bool:
        # remembering old solution, need to go through all solutions
        s = s.lower()   # case insensitive

        cleaned = ""
        for char in s:
            if char.isalnum():
                cleaned += char

        reverse = "".join(reversed(cleaned))

        return reverse == cleaned