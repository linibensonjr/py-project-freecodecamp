'''Palindrome'''

word_list = []
while len(word_list) != 1:
    word = input('Enter five(5) word, seperate each word with a comma(,): ')
    word_list.append(word)
#print (word_list)
for word in word_list:
    #Cast the word to lower case to handle mixed case
    ispalindrome = word[::-1].lower() == word.lower()
    if ispalindrome:
        print(word + ' is a palindrome')
    else:
        print(word + ' is not a palindrome')
# try:
#     word_list = words.split(',')
#     for word in word_list:


# except:
#     print("You didn't use commas")