class Solution:
    def isValid(self, s: str) -> bool:
        # add open brackets to the stack, when we encounter a close bracket, 
        # pop and make sure the corresponding open bracket is on the stack

        # we'll need a map of closing to open brackets
        pairs = { ")": "(", "}": "{", "]": "["}
        stack = []
        for bracket in s:
            if bracket not in pairs:
                stack.append(bracket)

            # we're dealing with a closing bracket
            elif not stack or stack.pop() != pairs[bracket]:
                return False

        return True if not stack else False
