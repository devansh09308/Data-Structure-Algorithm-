# Word Pattern – LeetCode 290
def check(pattern, s):
    word = s.split()
    
    if len(word) != len(pattern):
        return False
    
    map_p = {}
    map_s = {}

    for c1, c2 in zip(pattern, word):
        if c1 in map_p:
            if map_p[c1] != c2:
                return False
        else:
            if c2 in map_s:
                return False
            map_p[c1] = c2
            map_s[c2] = c1

    return True


pattern = "aaaa"
s = "dog cat cat dog"


print(check(pattern, s))