class Solution:
    def isPalindrome(self, s: str) -> bool:
        # transferred from leetcode
        phrase = s.lower()
        cleaned = ""

        for i, l in enumerate(phrase):
            if (l.isalnum()):
                cleaned += l
        
        reverse = "".join(reversed(cleaned)) # have to use reversed with join

        return reverse == cleaned