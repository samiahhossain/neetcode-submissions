class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # did by myself with hints, did not go over proper solutions
        output = []
        everything = 1
        zeroSeen = 0
        for num in nums:
            if num == 0 and zeroSeen == 0:
                zeroSeen += 1
            elif num == 0 and zeroSeen >= 1:
                zeroSeen = 2
                everything = 0
                break
            else:
                everything *= num

        for i in range(len(nums)):
            result = 1
            if nums[i] == 0 and zeroSeen == 1:
                result = everything
            elif zeroSeen > 1 or (nums[i] != 0 and zeroSeen == 1): 
                result = 0
            else:
                result = everything // nums[i]
            output.append(result)

        return output