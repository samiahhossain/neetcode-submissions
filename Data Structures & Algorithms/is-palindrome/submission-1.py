class Solution:
    def isPalindrome(self, s: str) -> bool:
        # remembering old solution, need to go through all solutions
        s = s.lower()   # case insensitive

        # ignoring non-alphanumeric chars
        cleaned = ""
        for char in s:
            if char.isalnum():
                cleaned += char

        # default function to reverse
        reverse = "".join(reversed(cleaned))

        return reverse == cleaned