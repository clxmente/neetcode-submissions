class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # brute force:
        #   iterate all subsequent values and keep track of the max
        #   if LT max, continue subbing with currMax
        #   else; iterate again for new max and sub, repeat

        for left in range(len(arr)):
            curr_max = 0
            for right in range(left + 1, len(arr)):
                curr_max = max(curr_max, arr[right])
            
            arr[left] = curr_max
        
        arr[-1] = -1
        return arr
