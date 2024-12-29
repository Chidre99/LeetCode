class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []  # Initialize an empty stack

        # Define a helper function for operations
        def apply_operator(op, b, a):  # Note: b is popped first, then a
            if op == '+':
                return a + b
            elif op == '-':
                return a - b
            elif op == '*':
                return a * b
            elif op == '/':
                # Perform integer division with truncation toward zero
                return int(a / b)

        # Process each token
        for token in tokens:
            if token in {"+", "-", "*", "/"}:
                # If token is an operator, pop two elements and apply the operator
                b = stack.pop()
                a = stack.pop()
                stack.append(apply_operator(token, b, a))
            else:
                # If token is a number, push it onto the stack
                stack.append(int(token))

        # The result will be the last element in the stack
        return stack[0]
