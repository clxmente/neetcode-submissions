class Solution {
    public boolean isValid(String s) {
        // Strings are immutable in java so we'll need something mutable from the input
        Map<Character, Character> pairs = Map.of(
            ')', '(', 
            '}', '{', 
            ']', '[');

        Deque<Character> stack = new ArrayDeque<>();
        for (char c : s.toCharArray()) {
            if (pairs.containsKey(c)) {
                // closing bracket
                if (stack.isEmpty() || stack.pop() != pairs.get(c)) {
                    return false;
                }
            } else {
                // opening bracket
                stack.push(c);
            }
        }

        return stack.isEmpty();
    }
}
