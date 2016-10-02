import os
# IPND Stage 2 Final Project

# You've built a Mad-Libs game with some help from Sean.
# Now you'll work on your own game to practice your skills and demonstrate what you've learned.

# For this project, you'll be building a Fill-in-the-Blanks quiz.
# Your quiz will prompt a user with a paragraph containing several blanks.
# The user should then be asked to fill in each blank appropriately to complete the paragraph.
# This can be used as a study tool to help you remember important vocabulary!

# Note: Your game will have to accept user input so, like the Mad Libs generator,
# you won't be able to run it using Sublime's `Build` feature.
# Instead you'll need to run the program in Terminal or IDLE.
# Refer to Work Session 5 if you need a refresher on how to do this.

# To help you get started, we've provided a sample paragraph that you can use when testing your code.
# Your game should consist of 3 or more levels, so you should add your own paragraphs as well!

sample = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''

# The answer for ___1___ is 'function'. Can you figure out the others?

# We've also given you a file called fill-in-the-blanks.pyc which is a working version of the project.
# A .pyc file is a Python file that has been translated into "byte code".
# This means the code will run the same as the original .py file, but when you open it
# it won't look like Python code! But you can run it just like a regular Python file
# to see how your code should behave.

# Hint: It might help to think about how this project relates to the Mad Libs generator you built with Sean.
# In the Mad Libs generator, you take a paragraph and replace all instances of NOUN and VERB.
# How can you adapt that design to work with numbered blanks?

# If you need help, you can sign up for a 1 on 1 coaching appointment: https://calendly.com/ipnd1-1/20min/

#----------------------------------
# ks81's Fill-in-the-Blanks quiz
#
# Developer: Kenneth Soerensen
# copyright: 2016 Kenneth Soerensen
#
#----------------------------------


def welcome():
    print """
#################################################
#                                               #
#   Welcome to ks81's Fill-in-the-Blanks quiz   #
#                   a game by                   #
#               Kenneth Soerensen               #
#                                               #
#################################################

"""

def get_username_from_user():
    username = raw_input("Please enter your name? ")

    if username == "":
        username = "NoName"

    print os.linesep + "Hello " + username
    
    # We only care if the user enter "n" for No, other input is regarded as Yes.
    # You can than just click "Enter" if you want to continue.
    if raw_input("Is this correct? (y/n) " ).lower() == 'n':
        username = get_username_from_user()

    return username


def difficulty(level):
    if level.lower() == "easy":
        return 0

    elif level.lower() == "medium":
        return 1

    elif level.lower() == "hard":
        return 2
    
    # Just to be on the safe side, but can make it harder to spot a bug/error this way.
    # Could have returned/raised an error, but for this project we just return 0 for easy.
    return 0


def get_difficulty_level(username):
    print os.linesep + username + """ please select a game difficulty by typing it in!
Use full word or first letter.
Possible choices includes (e)asy, (m)edium, and (h)ard."""

    difficulty_level = None

    # Convert input to lowercase for ease of use. 
    user_input = raw_input("What is your choise?" + os.linesep).lower()

    difficulty_level_text = ["EASY", "MEDIUM", "HARD"]
    feedback_text = os.linesep + "You have choosen LVL as your difficulty level"

    if user_input == "":
        print os.linesep + "You did not correctly choose your difficulty level"
        return get_difficulty_level(username)
        
    if (user_input[0] == 'e'):
        difficulty_level = difficulty("easy")
        print feedback_text.replace("LVL", difficulty_level_text[difficulty_level])

    elif user_input[0] == 'm':
        difficulty_level = difficulty("medium")
        print feedback_text.replace("LVL", difficulty_level_text[difficulty_level])

    elif user_input[0] == 'h':
        difficulty_level = difficulty("hard")
        print feedback_text.replace("LVL", difficulty_level_text[difficulty_level])

    else:
        print os.linesep + "You did not correctly choose your difficulty level"
        difficulty_level = get_difficulty_level(username)

    return difficulty_level


def get_quiz_blanks(difficulty_level):
    if difficulty_level == difficulty("easy"):
        return ["___1___", "___2___", "___3___", "___4___"]

    elif difficulty_level == difficulty("medium"):
        return ["___1___", "___2___", "___3___", "___4___", "___5___"]

    elif difficulty_level == ifficulty("hard"):
        return ["___1___", "___2___", "___3___", "___4___", "___5___", "___6___"]
        
    # Just to be on the safe side, but can make it harder to spot a bug/error this way.
    # Could have returned/raised an error, but for this project we just return quiz blanks for easy.
    return ["___1___", "___2___", "___3___", "___4___"]


def get_number_of_guesses(difficulty_level):
    if difficulty_level == difficulty("easy"):
        return 5

    elif difficulty_level == difficulty("medium"):
        return 4

    elif difficulty_level == ifficulty("hard"):
        return 3
    
    # Just to be on the safe side, but can make it harder to spot a bug/error this way.
    # Could have returned/raised an error, but for this project we just return 5 guesses for easy.
    return 5


def get_quiz_text(difficulty_level):

    easy_quiz_text = """A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions."""

    if difficulty_level == difficulty("easy"):
        return easy_quiz_text

    elif difficulty_level == difficulty("medium"):
        return "medium"
    elif difficulty_level == ifficulty("hard"):
        return "hard"

    # Just to be on the safe side, but can make it harder to spot a bug/error this way.
    # Could have returned/raised an error, but for this project we just return the fill_in_the_blank text for easy.
    return easy_quiz_text




def game():
    username = ""
    difficulty_level = None
    
    welcome()
    username = get_username_from_user()
    difficulty_level = get_difficulty_level(username)
    
    print os.linesep + "You will get %s guesses per problem." % (get_number_of_guesses(difficulty_level)) + os.linesep
    

def main():
    game()


if __name__ == "__main__":
    main()