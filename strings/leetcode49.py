def match(strs):
    count = {}

    for word in strs:
        key = ''.join(sorted(word))

        if key not in count:
            count[key] = []
        count[key].append(word)
        
    return list(count.values())

strs = ["eat","tea","tan","ate","nat","bat"]

print(match(strs))