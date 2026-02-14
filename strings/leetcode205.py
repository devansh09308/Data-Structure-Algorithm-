# 205. Isomorphic Strings
def maping(s, t):
    map_s = {}
    map_t = {}

    for c1,c2 in zip(s, t):
        if c1 in map_s:
            if map_s[c1] != c2:
                return False
        if c2 in map_t:
            if map_t[c2] != c1:
                return False    
        
        map_s[c1] = c2
        map_t[c2] = c1

    return True


s = "paper"
t = "title"

print(maping(s,t))