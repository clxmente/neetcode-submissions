class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int currCount = 0;
        int maxCount = 0;

        for (int n : nums) {
            if (n == 1) {
                currCount += 1;
            } else {
                currCount = 0;
            }
            maxCount = Math.max(currCount, maxCount);
        }

        return maxCount;
    }
}