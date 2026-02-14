from collections import deque

q1 = deque()
q2 = deque()

def push(x):
    q2.append(x)
    # Move all elements from q1 to q2
    while q1:
        q2.append(q1.popleft())
    # Swap q1 and q2
    global q1, q2
    q1, q2 = q2, q1

def pop():
    if q1:
        return q1.popleft()
    return None

def top():
    if q1:
        return q1[0]
    return None

def empty():
    return not q1
