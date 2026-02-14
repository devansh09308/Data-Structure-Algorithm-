print('hello Google Colab!')

a = 1
b = 2

print(a + b)

# res = input('Enter something: ')
# res2 = int(res)

# if res2 % 2 == 0:
#     print('even')
# else:
#     print('odd')



word = input('Enter a word: ')

reverse = word[::-1]

if word == reverse:
    print('palindrome')
else:
    print('not palindrome')