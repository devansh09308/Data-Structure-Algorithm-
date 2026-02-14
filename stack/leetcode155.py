stack = []
min_stack = []

def push(x):
    stack.append(x)
    if not min_stack or x <= min_stack[-1]:
        min_stack.append(x)

def pop():
    if stack:
        val = stack.pop()
        if val == min_stack[-1]:
            min_stack.pop()

def top():
    if stack:
        return stack[-1]
    return None

def getMin():
    if min_stack:
        return min_stack[-1]
    return None