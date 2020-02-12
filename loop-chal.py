# Print odd nums except 57.
my_numbers = range(0, 100)

for i in my_numbers:
    if i % 2 == 0 or i == 57:
        continue
    print(i)


# Longest name
names = ['Sheng', 'Kevin', 'Audrey', 'KJ', 'Delilah', 'Josh', 'Mack', 'Rey']

longest_name = ''

for name in names:
    while len(longest_name) < len(name):
        longest_name = name

print(f'Longest name: {longest_name}')


# Refractor
word_list = ['Java', 'Golang', 'Python', 'JavaScript']
words = [word for word in word_list if len(word) > 5]
print(words)
