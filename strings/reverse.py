def reverse_string(s):
    rev = ''
    i = 0
     
    length = 0

    for _ in s:
        length += 1

    i = length - 1

    while i >= 0:
        rev += s[i]
        i -= 1

    return rev

s= input('Enter a word: ')
reverse = reverse_string(s)

print(reverse)

if reverse == s:
    print('palindrom')
else:
    print ('not a palindrome')