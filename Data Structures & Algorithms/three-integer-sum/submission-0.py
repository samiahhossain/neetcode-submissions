class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # looked at old solution, need to closely analyze

        nums.sort() # keep forgetting this function exists
        indexes = []

        n = len(nums)
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue    # skip duplicates
            
            # run the two pointer approach on the elements to 
            # the right of index i as the array is sorted.
            left = i + 1
            right = n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    indexes.append([nums[i], nums[left], nums[right]])

                    # skip duplicates
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # while left < right and nums[right] == nums[right - 1]:
                    #     right -= 1
                    # why no skipping of right duplicates needed?

                    left += 1
                    right -= 1

                elif total < 0: # sum too small
                    left += 1
                else:
                    right -= 1  # sum too big

        return indexes
