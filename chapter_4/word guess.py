#computer picks random word and player has to guess.  computer tells player how many letters are in the word.  player gets 5 chances to guess the word.  the pc can only respond yes or no.

import random

WORDS = ("apple", "pear", "peach", "cherry", "grape")

word = random.choice(WORDS)

size = len(word)
print("the computer has selected a word at random, you job is to guess what that word is")
print("your word is ", size, "letters long")

guess = input("what do you think the word is?")
count = 0

while guess != word:
    print("that is incorrect, guess again")
    guess = input("next guess?")
    count +=1
    if count == 5:
        print("too many guesses, you lose")
        break
if guess == word:
    print("that is correct!!!")




#count = 0
#while user != the_number:

 #   if user > the_number:
  #   print ("Lower")
#
 #   elif user < the_number:
  #   print ("Higher")
#
 #   user = int(input("What's the number?"))
  #  count += 1
   # if count == 5: # change this number to change the number of guesses
    #    break # exit this loop when the above condition is met