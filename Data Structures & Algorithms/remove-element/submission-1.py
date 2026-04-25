class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # when we find val, swap to the end of the array, decreasing the "end" each time we find and swap

        # when we find val, shift entire array left.

        i = 0
        n = len(nums)
        while i < n:
            if nums[i] == val:
                n -= 1
                nums[i] = nums[n]
            else:
                i += 1
        
        return n