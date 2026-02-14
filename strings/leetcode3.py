# 3. Longest Substring Without Repeating Characters

def string(str):
    map = {}
    longest = 0
    for ch in str:
        if ch not in map:
            map[ch] = map.get(ch,0) + 1
        else:
            check = len(map)
            if check > longest:
                longest = check
                map ={}
    return longest
        
s = "pwwkew"
print(string(s))