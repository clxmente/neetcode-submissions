class Solution {
    public int[] replaceElements(int[] arr) {
        int[] newList = new int[arr.length];
        int currMax = -1;

        for (int i = arr.length - 1; i > -1; i--) {
            newList[i] = currMax;
            currMax = Math.max(currMax, arr[i]);
        }

        return newList;
    }
}