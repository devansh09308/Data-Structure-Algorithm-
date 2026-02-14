# Ransom Note – LeetCode 383
def check(ransomNote, magazine):
    map1 = {}

    for ch in magazine:
        map1[ch] = map1.get(ch, 0) + 1
    
    for ch in ransomNote:
        if ch not in map1:
            return False
        elif map1[ch] > 0:
            map1[ch] -=1
        else:
            return False
        
    return True

ransomNote = "aa"
magazine = "aab"

print(check(ransomNote, magazine))