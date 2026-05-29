class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token != "+" and token != "*" and token != "-" and token != "/":
                stack.append(int(token))

            if token == "+":
                num2, num1 = stack.pop(), stack.pop()
                stack.append(int(num1 + num2))

            if token == "-":
                num2, num1 = stack.pop(), stack.pop()
                stack.append(int(num1 - num2))

            if token == "*":
                num2, num1 = stack.pop(), stack.pop()
                stack.append(int(num1 * num2))  

            if token == "/":
                num2, num1 = stack.pop(), stack.pop()
                stack.append(int(num1 / num2))
        
        return stack[-1]