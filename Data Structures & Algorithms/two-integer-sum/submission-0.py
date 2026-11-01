class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevNums = {}

        for i, num in enumerate(nums):
            num2 = target - num
            if num2 in prevNums:
                return [prevNums[num2], i]
            prevNums[num] = i

        return []