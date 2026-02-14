# 14) Find the Difference – LeetCode 389
def count(s, t):
    result = 0

    for ch in s:
        result = result ^ ord(ch)
    for ch in t:
        result = result ^ ord(ch)
    return chr(result)

s = ""
t = "y"

print(count(s,t))