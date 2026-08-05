class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        # Create an empty stack that will store numbers.
        stack = []

        # Go through every token in the expression.
        for token in tokens:

            # If the token is NOT an operator,
            # then it must be a number.
            if token not in ["+", "-", "*", "/"]:

                # Convert the string into an integer
                # and push it onto the stack.
                stack.append(int(token))

            else:
                # The token is an operator.
                # We need two numbers to perform the operation.

                # Pop the second number first.
                second = stack.pop()

                # Pop the first number second.
                first = stack.pop()

                # Perform the correct operation.
                if token == "+":
                    stack.append(first + second)

                elif token == "-":
                    stack.append(first - second)

                elif token == "*":
                    stack.append(first * second)

                elif token == "/":
                    # int(a / b) truncates toward zero,
                    # which is exactly what the problem asks for.
                    stack.append(int(first / second))

        # After processing all tokens,
        # the stack will contain exactly one value:
        # the final answer.
        return stack[0]