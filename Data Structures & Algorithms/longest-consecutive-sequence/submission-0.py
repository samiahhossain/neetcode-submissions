class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # looked at solution
        numSet = set(nums)  # convert to hash set for O(1) lookups
        longest = 0

        for num in numSet:
            if (num - 1) not in numSet:
                length = 1
                while (num + length) in numSet: # keep moving up by 1 if exist
                    length += 1
                longest = max(longest, length)

        return longest