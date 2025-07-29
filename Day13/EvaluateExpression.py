def evaluate_postfix(expression_string):
    stack = []
    tokens = expression_string.split()

    for token in tokens:
        if token.isdigit():
            stack.append(int(token))
        elif '.' in token:
            stack.append(float(token))
        elif token in ('+', '-', '*', '/'):
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(a / b)  
        else:
            raise ValueError(f"Unknown token: {token}")

    return stack[0]  

print(evaluate_postfix("2 3 +"))          # Output: 5
print(evaluate_postfix("2 3 4 * +"))      # Output: 14
print(evaluate_postfix("10 5 / 2 +"))     # Output: 4.0

