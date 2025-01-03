#import random module
import random

print("\nWelcome to the Band Name Generator.\n")

#def is defining a function, which has a proces inbetween and then must return something
#random_line is the function
#file_name is a variable
#spltlines is used to break the string when the file is read into different line. The string is broken into lines where the computer detects a new line
#random.choice chooses randomly from one of the lines in the file we opened and read
def random_line(filename):
    a_line = open(filename).read().splitlines()
    return random.choice(a_line)

#assign file to file_name variable to use when needed
#constants should be capitolized
FILE_NAME = "question_bank"

#use the file name  to locate the file we are taking from
#prompt for answer(input) to the random questions
question1 = input(random_line(FILE_NAME) + "\n")
question2 = input(random_line(FILE_NAME) + "\n")

#add responses together
#f allows variables in strings if they are in curly braces(no plus sign needed)
band_name = f"{question1} {question2}"
print(f"Your band name could be {band_name}")
