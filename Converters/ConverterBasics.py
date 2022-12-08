from Models.Stack import Stack


class ConverterBasics:
    def __init__(self):
        self.stack = Stack()
        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    def hasLessOrEqualPriority(self, op1, op2):
        if op1 not in self.precedence:
            return False
        if op2 not in self.precedence:
            return False
        return self.precedence[op1] <= self.precedence[op2]

    def hasLessPriority(self, op1, op2):
        if op1 not in self.precedence:
            return False
        if op2 not in self.precedence:
            return False
        return self.precedence[op1] < self.precedence[op2]

    def hasEqualPriority(self, op1, op2):
        if op1 not in self.precedence:
            return False
        if op2 not in self.precedence:
            return False
        return self.precedence[op1] == self.precedence[op2]

    @staticmethod
    def isOperator(inpu):
        ops = ['+', '-', '/', '*']
        return inpu in ops

    @staticmethod
    def isOperand(char):
        return char.isalpha() or char.isdigit()

    @staticmethod
    def isOpenParenthesis(char):
        return char == '('

    @staticmethod
    def isCloseParenthesis(char):
        return char == ')'

    @staticmethod
    def expressionFormatter(expr):
        return expr.replace(" ", "")
