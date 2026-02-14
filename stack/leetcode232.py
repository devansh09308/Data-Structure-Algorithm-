in_stack = []
out_stack = []

def push(x):
    in_stack.append(x)

def pop():
    if not out_stack:
        while in_stack:
            out_stack.append(in_stack.pop())
    if out_stack:
        return out_stack.pop()
    return None

def peek():
    if not out_stack:
        while in_stack:
            out_stack.append(in_stack.pop())
    if out_stack:
        return out_stack[-1]
    return None

def empty():
    return not in_stack and not out_stack
