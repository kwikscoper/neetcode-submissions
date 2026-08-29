class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {'+', '-', '*', '/'}
        stack = []

        for token in tokens:
            if token in ops:
                #pop top two items in stack
                a = stack.pop()
                b = stack.pop()
                
                if token == '+':
                    c = b + a
                elif token == '-':
                    c = b - a
                elif token == '*':
                    c = b * a
                else:
                    c = b / a

                stack.append(int(c))

            else:
                stack.append(int(token))

        return stack[0]