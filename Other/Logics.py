from Models.Stack import Stack


def OperatorPriority(x):
    if x in "+-":
        return 1
    elif x in "*/":
        return 2
    elif x in "^":
        return 3
    return 0


def InfixToPrefix(infix_arr):
    # Converts Infix to Prefix Notation
    output = ""
    for char in infix_arr[::-1]:
        if char == '(':
            output += ")"
        elif char == ')':
            output += "("
        else:
            output += char

    output = InfixToPostfix(output)
    return output[::-1]


def InfixToPostfix(infix_arr):
    # Converts Infix to Postfix Notation
    stack = Stack()
    output = ""
    for char in infix_arr:
        if char not in "+-*/^()":
            output += char
        elif char == '(':
            stack.push('(')
        elif char == ')':
            while stack and stack.top() != '(':
                output += stack.pop()
            stack.pop()
        else:
            while stack and stack.top() != '(' and OperatorPriority(char) <= OperatorPriority(stack.top()):
                output += stack.pop()
            stack.push(char)
    while stack:
        output += stack.pop()
    return output


def PostfixToPrefix(post_arr):
    # Converts Postfix to Prefix Notation
    stack = Stack()
    for char in post_arr:
        if char in "+-*/^":
            # pop two operands from stack
            op1 = stack.top()
            stack.pop()
            op2 = stack.top()
            stack.pop()
            temp = char + op2 + op1
            stack.push(temp)
        else:
            stack.push(char)
    output = stack.pop()
    return output


def PrefixToPostfix(pre_arr):
    # Converts Prefix to Postfix Notation
    stack = Stack()
    arr = pre_arr[::-1]
    for char in arr:
        if char not in "+-*/^":
            op1 = stack.pop()
            op2 = stack.pop()
            temp = op1 + op2 + char
            stack.push(temp)
        else:
            stack.push(char)
    output = stack.pop()
    return output


def PrefixToInfix(pre_arr):
    # Converts Prefix to Infix Notation
    stack = Stack()
    i = len(pre_arr) - 1
    while i >= 0:
        if pre_arr[i] not in "+-*/^()":
            stack.push(pre_arr[i])
            i -= 1
        else:
            temp = "(" + stack.pop() + pre_arr[i] + stack.pop() + ")"
            stack.push(temp)
            i -= 1
    output = stack.pop()
    return output


def PostfixToInfix(post_arr):
    # Converts Postfix to Infix Notation
    stack = Stack()
    for char in post_arr:
        if char not in "+-*/^()":
            stack.push(char)
        else:
            op1 = stack.pop()
            op2 = stack.pop()
            temp = "(" + op2 + char + op1 + ")"
            stack.push(temp)
    output = stack.pop()
    return output
