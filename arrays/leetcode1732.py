# 1732. Find the Highest Altitude
def highestGain(gain):
    sum = 0
    highest = 0

    for g in gain:
        sum += g
        highest = max(sum, highest)

    return highest

gain = [-4,-3,-2,-1,4,3,2]
print(highestGain(gain))