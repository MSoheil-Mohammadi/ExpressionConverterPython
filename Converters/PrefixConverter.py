from Converters.ConverterBasics import ConverterBasics
from Models.Stack import Stack


class PrefixConverter(ConverterBasics):
    def toInfix(self, expr):
        expr = self.expressionFormatter(expr)
        expr = expr[::-1]
        self.stack = Stack()
        for char in expr:
            if not self.isOperator(char):
                self.stack.push(char)
            else:
                temp = "(" + self.stack.pop() + char + self.stack.pop() + ")"
                self.stack.push(temp)
        output = self.stack.pop()
        return output

    def toPostfix(self, expr):
        expr = self.expressionFormatter(expr)
        expr = expr[::-1]
        self.stack = Stack()
        for char in expr:
            if self.isOperand(char):
                self.stack.push(char)
            else:
                op1 = self.stack.pop()
                op2 = self.stack.pop()
                temp = op1 + op2 + char
                self.stack.push(temp)
        output = self.stack.pop()
        return output

    def convert(self, expr):
        print(expr, self.toPostfix(expr), self.toInfix(expr))
