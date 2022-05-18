'''Biography info '''
'''Ask a user for their personal information one question at a time. 
Then check that the information they entered is valid. Finally, print a summary of all the information they entered back to them.
'''

print("Hello there, hope you're habing a good time.\n Let's get to know you!")
name = input("What's your name? ")

if len(name) == 1:
        name = input("Ouch! that's an invalid input \nThat was too shortWhat's your name? ")
else:
    dob_day = input("What's your day were you born? ")
    dob_mth = input("What month were you born? ")
    dob_yr = input("How about the year? ")
    address = input("Where do you live? ")
    goals = input("What are your personal goals? ")

    print("Your personal information")
    print("- Name:", name)
    print("- Date of birth: {} {}, {}".format(dob_mth, dob_day, dob_yr))
    print("- Address: ", address)
    print("- Personal goals: ", goals)