from Converters.ConverterBasics import ConverterBasics
from Models.Stack import Stack


class InfixConverter(ConverterBasics):
    def toPostfix(self, expr):
        expr = self.expressionFormatter(expr)
        self.stack = Stack()
        output = ''

        for char in expr:
            if self.isOperand(char):
                output += char
            elif self.isOpenParenthesis(char):
                self.stack.push(char)
            elif self.isCloseParenthesis(char):
                while self.stack and self.stack.top() != '(':
                    output += self.stack.pop()
                self.stack.pop()
            else:
                while self.stack and self.stack.top() != '(' and \
                        self.hasLessOrEqualPriority(char, self.stack.top()):
                    output += self.stack.pop()
                self.stack.push(char)

        while self.stack:  # then we empty the stack.
            output += self.stack.pop()

        return output

    def toPrefix(self, expr):
        expr = self.expressionFormatter(expr)
        self.stack = Stack()
        expr = '(' + expr + ')'
        expr = expr[::-1]
        output = ""
        for char in expr:
            if self.isOperand(char):
                output += char
            elif char == ")":
                self.stack.push(char)
            elif char in "+-*/^":
                if char == "^":
                    while self.hasLessOrEqualPriority(char, self.stack.top()):
                        output += self.stack.pop()
                else:
                    while self.hasLessPriority(char, self.stack.top()):
                        output += self.stack.pop()
                self.stack.push(char)
            elif char == "(":
                while not self.stack.is_empty():
                    char1 = self.stack.pop()
                    if char1 == ')':
                        break
                    output += char1
        while not self.stack.is_empty():
            output += self.stack.pop()
        return output[::-1]

    def convert(self, expr):
        print(expr, self.toPostfix(expr), self.toPrefix(expr))
