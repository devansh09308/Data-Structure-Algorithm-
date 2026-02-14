s = "aabbc"

freq = {}

for ch in s:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

print(freq)

nums = [4, 3, 1, 4]

seen = set()

for num in nums:
    if num in seen:
        print("Duplicate =", num)
    seen.add(num)
