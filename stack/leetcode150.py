def arithmetic(token):
    stack = []

    for t in token:
        if t not in "+-*/":
            stack.append(int(t))
        else:
            b = stack.pop()
            a = stack.pop()

            if t == "+":
                stack.append(a + b)
            elif t == "-":
                stack.append(a - b)
            elif t == "*":
                stack.append(a * b)
            else:
                stack.append(int(a / b))  # truncate toward 0

    return stack[0]


token = ["2","1","+","3","*"]
print(arithmetic(token))
