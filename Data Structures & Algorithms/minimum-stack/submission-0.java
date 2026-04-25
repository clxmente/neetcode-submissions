class MinStack {
    private int min = Integer.MAX_VALUE;
    final List<Integer> stack;
    public MinStack() {
        this.stack = new ArrayList<Integer>();
    }
    
    public void push(int val) {
        this.stack.add(val);
        this.min = Math.min(this.min, val);
    }
    
    public void pop() {
        this.stack.remove(this.stack.size() - 1);
        
        int currMin = Integer.MAX_VALUE;
        // recalculate minimum
        for (int n : this.stack) {
            currMin = Math.min(n, currMin);
        }
        this.min = currMin;
    }
    
    public int top() {
        return this.stack.get(this.stack.size() - 1);
    }
    
    public int getMin() {
        return this.min;
    }
}
