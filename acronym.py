'''What's the Acronym'''

full_meaning = input('Enter the full meaning of word: ')
word_list = full_meaning.title().split()
for i in word_list:
    acronym = ''.join(i[0])
print(acronym)