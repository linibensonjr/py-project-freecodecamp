'''Word count script'''

text = input("what's on your mind today? ")
text_count = text.split()
print("Oh nice, you just told me what's on your mind in {} words!".format(len(text_count)))