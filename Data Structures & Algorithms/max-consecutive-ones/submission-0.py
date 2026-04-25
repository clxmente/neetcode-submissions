class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0
        curr_count = 0

        for n in nums:
            if n == 1:
                curr_count += 1
            else:
                curr_count = 0
            
            max_count = max(max_count, curr_count)

        return max_count