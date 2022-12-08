from Converters.ConverterBasics import ConverterBasics
from Models.Stack import Stack


class PostfixConverter(ConverterBasics):
    def toInfix(self, expr):
        expr = self.expressionFormatter(expr)
        self.stack = Stack()
        for char in expr:
            if self.isOperand(char):
                self.stack.push(char)
            else:
                op1 = self.stack.pop()
                op2 = self.stack.pop()
                temp = "(" + op2 + char + op1 + ")"
                self.stack.push(temp)
        output = self.stack.pop()
        return output

    def toPrefix(self, expr):
        expr = self.expressionFormatter(expr)
        self.stack = Stack()
        for char in expr:
            if self.isOperand(char):
                self.stack.push(char)
            else:
                op1 = self.stack.top()
                self.stack.pop()
                op2 = self.stack.top()
                self.stack.pop()
                temp = char + op2 + op1
                self.stack.push(temp)
        output = self.stack.pop()
        return output

    def convert(self, expr):
        print(expr, self.toInfix(expr), self.toPrefix(expr))
