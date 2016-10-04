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


def difficulty_index_list():

    return ["custom", "easy", "medium", "hard", "very hard", "ultra hard"]


def input_check_list():

    return ["c", "e", "m", "h", "v", "u"]


def difficulty_level_feedback_text():

    return ["CUSTOM", "EASY", "MEDIUM", "HARD", "VERY HARD", "ULTRA HARD"]


def difficulty(level):

    index_list = difficulty_index_list()

    for index in index_list:
        if level.lower() in index:
            return index_list.index(index)
    
    return index_list.index("easy")


def get_difficulty_level_from_user(username):

    index_list = difficulty_index_list()
    user_input_check_list = input_check_list()
    difficulty_level_text = difficulty_level_feedback_text()

    # Convert input to lowercase for ease of use. 
    user_input = raw_input(username + ", what is your choise? ").lower()

    if user_input in user_input_check_list:
        difficulty_level = difficulty(index_list[user_input_check_list.index(user_input[0])])

        print os.linesep + username + ", you have choosen %s as your difficulty level" % (difficulty_level_text[difficulty_level])
        return difficulty_level

    print os.linesep + username + ", you did not correctly choose your difficulty level"
    return get_difficulty_level_from_user(username)


def get_game_difficulty_level_from_user(username):

    print os.linesep + username + """, please select a game difficulty by typing it in!
Use full word or first letter.
Possible choices includes (e)asy, (m)edium, (h)ard, (v)ery hard, (u)ltra hard and (c)ustom."""

    return get_difficulty_level_from_user(username)


def get_custom_guesses_from_user():

    user_input = raw_input("How many guesses do you want? ")

    if not user_input.isdigit():
        print "Please enter a number representing your number of guesses!"
        return get_custom_guesses_from_user()

    if int(user_input) < 1:
        print "Please enter a number from 1 and upwords!"
        return get_custom_guesses_from_user()

    return int(user_input)


def get_number_of_guesses(difficulty_level):
    
    guesses_per_difficulty_level = {"easy" : 5, "medium" : 4, "hard" : 3, "very hard" : 2, "ultra hard" : 1}
    difficulty_index = difficulty_index_list()

    if difficulty_level == difficulty("custom"):
        return get_custom_guesses_from_user()

    for k, v in guesses_per_difficulty_level.items():
        if k == difficulty_index[difficulty_level]:
            return v
    
    # Just to be on the safe side, but can make it harder to spot a bug/error this way.
    # Could have returned/raised an error, but for this project we just return 5 guesses for easy.
    return guesses_per_difficulty_level["easy"]


def get_quiz_text_and_answer():

    easy_quiz_text = """A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions."""

    easy_quiz_answer = ["answer 1", "answer 2", "answer 3", "answer 4"]

    medium_quiz_text = """___1___ ___2___ ___3___ ___4___ ___5___"""

    medium_quiz_answer = ["answer 1", "answer 2", "answer 3", "answer 4", "answer 5"]

    hard_quiz_text = """___1___ ___2___ ___3___ ___4___ ___5___ ___6___"""

    hard_quiz_answer = ["answer 1", "answer 2", "answer 3", "answer 4", "answer 5", "answer 6"]

    very_hard_quiz_text = """___1___ ___2___ ___3___ ___4___ ___5___ ___6___ ___7___"""

    very_hard_quiz_answer = ["answer 1", "answer 2", "answer 3", "answer 4", "answer 5", "answer 6", "answer 7"]

    ultra_hard_quiz_text = """___1___ ___2___ ___3___ ___4___ ___5___ ___6___ ___7___ ___8___"""

    ultra_hard_quiz_answer = ["answer 1", "answer 2", "answer 3", "answer 4", "answer 5", "answer 6", "answer 7", "answer 8"]

    return {"easy" : [easy_quiz_text, easy_quiz_answer], "medium" : [medium_quiz_text, medium_quiz_answer], "hard" : [hard_quiz_text, hard_quiz_answer], "very hard" : [very_hard_quiz_text, very_hard_quiz_answer], "ultra hard" : [ultra_hard_quiz_text, ultra_hard_quiz_answer]}



def get_quiz(difficulty_level, username, quiz):

    index_list = difficulty_index_list()
    quiz_blanks = []

    if difficulty_level == difficulty("custom"):
        difficulty_level = get_quiz_difficulty_level_when_custom(difficulty_level, username)

    for k, v in quiz.items():
        if index_list[difficulty_level] == k:

            count = len(v[1])
            i = 1
            while i <= count:
                quiz_blanks.append("___%s___" % (i))
                i += 1

            return v[0], v[1], quiz_blanks

    return None

def get_quiz_difficulty_level_when_custom(difficulty_level, username):

    if difficulty_level == difficulty("custom"):
        print  os.linesep + username + """, since you have choosen custom difficulty you need to choose which quiz text dificulty you want to try.
Please select a difficulty by typing it in!
Use full word or first letter.
Possible choices includes (e)asy, (m)edium, (h)ard, (v)ery hard and (u)ltra hard.
"""

    quiz_difficulty_level = get_difficulty_level_from_user(username)

    if quiz_difficulty_level == difficulty("custom"):
        print os.linesep + username + ", you can not choose CUSTOM, please choose again!"
        quiz_difficulty_level = get_difficulty_level_from_user(username)

    return quiz_difficulty_level


def quiz_blank_in_pos(word, quiz_blank):
    if quiz_blank in word:
        return quiz_blank
    return None


def replace_word(quiz_text, quiz_blank, user_quiz_answer):

    replaced_quiz_text = []

    for word in quiz_text:
        replacement = quiz_blank_in_pos(word, quiz_blank)
        if replacement != None:
            word = word.replace(replacement, user_quiz_answer)
            replaced_quiz_text.append(word)
        else:
            replaced_quiz_text.append(word)

    return replaced_quiz_text


def game():
    username = ""
    difficulty_level = None
    number_of_guesses = None
    quiz_text= ""
    quiz_answer = []
    quiz_blanks = []
    
    welcome()
    username = get_username_from_user()
    
    difficulty_level = get_game_difficulty_level_from_user(username)

    number_of_guesses = get_number_of_guesses(difficulty_level)

    print os.linesep + "You will get %s guesses per problem." % (number_of_guesses) + os.linesep
    
    quiz_text, quiz_answer, quiz_blanks = get_quiz(difficulty_level, username, get_quiz_text_and_answer())


def main():
    game()


if __name__ == "__main__":
    main()