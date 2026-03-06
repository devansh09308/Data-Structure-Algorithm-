def validParanthesis(sh):
    stack = []
    mapping = {')' : '(', '}' : '{', ']' : '['}

    for ch in sh:
        if ch in mapping:
            if not stack or stack[-1] != mapping[ch]:
                return False
            stack.pop()
        else:
            stack.append(ch)

    if not stack:
        return True
    else:
        return False


sh = "([)]"
    
print(validParanthesis(sh))