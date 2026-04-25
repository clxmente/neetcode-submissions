class Solution {
    public int calPoints(String[] operations) {
        int score = 0;
        List<Integer> stack = new ArrayList<>();

        for (String op : operations) {
            if (op.equals("+")) {
                // add to the running total
                int newScore = stack.get(stack.size() - 2) + stack.get(stack.size() - 1);
                score += newScore;
                stack.add(newScore);
            } else if (op.equals("D")) {
                int newScore = stack.get(stack.size() - 1) * 2;
                score += newScore;
                stack.add(newScore);
            } else if (op.equals("C")) {
                score -= stack.remove(stack.size() - 1);
            } else {
                int newScore = Integer.valueOf(op);
                score += newScore;
                stack.add(newScore);
            }
        }

        return score;
    }
}