from Models.Node import Node
from Models.Stack import Stack


def postfix_draw(expr):
    stack = Stack()
    Operators = {'+', '-', '*', '/', '(', ')', '^'}
    for char in expr:
        if char in Operators:
            right = stack.pop()
            left = stack.pop()
            stack.push(Node(char, left, right))
        else:
            stack.push(Node(char))
    root = stack.pop()
    return root


def prefix_draw(expr):
    stack = Stack()
    Operators = {'+', '-', '*', '/', '(', ')', '^'}
    for char in reversed(expr):
        if char in Operators:
            right = stack.pop()
            left = stack.pop()
            stack.push(Node(char, left, right))
        else:
            stack.push(Node(char))
    root = stack.pop()
    return root
