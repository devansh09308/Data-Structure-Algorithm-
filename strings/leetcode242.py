def match(s,t):
    if len(s) != len(t):
        return False
    count = {}
    for ch in s:
        count[ch] = count.get(ch,0) + 1
    for ch in t:
        if ch not in count:
            return False
        else:
            count[ch] -= 1
        if count[ch] == 0:
            del count[ch]

    return len(count) == 0

s = "anagram"
t = "nagaram"

print(match(s,t))