class Solution {
    public int calPoints(String[] operations) {
        int[] stack = new int[operations.length];
        int top = -1;
        int score = 0;

        for (String op : operations) {
            if (op.equals("+")) {
                int newScore = stack[top] + stack[top - 1];
                score += newScore;
                stack[++top] = newScore; 
            } else if (op.equals("D")) {
                int newScore = stack[top] * 2;
                score += newScore;
                stack[++top] = newScore;
            } else if (op.equals("C")) {
                score -= stack[top];
                --top;
            } else {
                int newScore = Integer.valueOf(op);
                score += newScore;
                stack[++top] = newScore;
            }
        }
        return score;
    }
}