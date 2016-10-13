#----------------------------------
#
# IPND Stage 2 Final Project
#
#----------------------------------
# ks81's Fill-in-the-Blanks quiz
#
# Developer: Kenneth Soerensen
# 
# MIT License
#
# Copyright (c) 2016 Kenneth Soerensen
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
#----------------------------------

import os

# Print the welcome message
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

# Get the name the user want to use during the game from the user.
# Returnes the chossen username.
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

# A list of difficulty levels.
# Returns the difficulty index list.
def difficulty_index_list():

    return ["custom", "easy", "medium", "hard", "very hard", "ultra hard"]

# A list of input check characters.
# Returns the input check list.
def input_check_list():

    return ["c", "e", "m", "h", "v", "u"]

# A list of feedback text to the user based on what difficulty level is choosen.
# Returns the difficulty level feedback text list.
def difficulty_level_feedback_text():

    return ["CUSTOM", "EASY", "MEDIUM", "HARD", "VERY HARD", "ULTRA HARD"]

# Converting difficulty level from text to a number so we can use it easily 
# with lists and other indexes.
# Returns a number representing the difficulty level.
def difficulty(level):

    index_list = difficulty_index_list()

    for index in index_list:
        if level.lower() in index:
            return index_list.index(index)
    
    return index_list.index("easy")

# Get the difficulty level from the user.
# Returnes a number representing the difficulty level.
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

# Get the game difficulty level from the user.
# This will be the difficulty level of the game that the user will use.
# Returnes a number representing the difficulty level.
def get_game_difficulty_level_from_user(username):

    print os.linesep + username + """, please select a game difficulty by typing it in!
Use full word or first letter.
Possible choices includes (e)asy, (m)edium, (h)ard, (v)ery hard, (u)ltra hard and (c)ustom."""

    return get_difficulty_level_from_user(username)

# Get the number of guesses from the user when custom number of guesses is choosen.
# Returns the number of guesses.
def get_custom_guesses_from_user():

    user_input = raw_input("How many guesses do you want? ")

    if not user_input.isdigit():
        print "Please enter a number representing your number of guesses!"
        return get_custom_guesses_from_user()

    if int(user_input) < 1:
        print "Please enter a number from 1 and upwords!"
        return get_custom_guesses_from_user()

    return int(user_input)

# Get the number of guesses based on the game difficulty level choosen.
# Returns the number of guesses.
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

# Get quiz text and answers.
# Returns quiz text and answers.
def get_quiz_text_and_answer():

    easy_quiz_text = """___1___ are amongst the most popular ___2___ in Python. We can create them simply by 
enclosing characters in ___3___. Python treats single ___3___ the same as double ___3___. Creating strings 
is as simple as assigning a value to a ___4___."""

    easy_quiz_answer = ["Strings", "types", "quotes", "variable"]

    medium_quiz_text = """Python Loops! In general, ___2___s are ___1___  sequentially: The first ___2___ in 
a function is ___1___  first, followed by the second, and so on. There may be a situation when you need to 
execute a ___3___ of code several number of times. Programming ___4___ provide various control structures 
that allow for more ___5___ execution paths. A loop ___2___ allows us to execute a ___2___ or group of 
___2___s multiple times."""

    medium_quiz_answer = ["executed", "statement", "block", "languages", "complicated"]

    hard_quiz_text = """___1___ is a high-level, ___2___, interactive and object-oriented scripting language. 
___1___ is designed to be highly readable. It uses ___3___ keywords frequently where as other languages use 
punctuation, and it has fewer syntactical constructions than other languages. - ___1___ is Interpreted: 
___1___ is processed at runtime by the interpreter. You do not need to ___4___ your program before executing 
it. This is similar to PERL and PHP. - ___1___ is Interactive: You can actually sit at a ___1___ prompt and 
interact with the interpreter directly to write your programs. - ___1___ is Object-Oriented: ___1___ supports
Object-Oriented style or technique of ___5___ that encapsulates code within objects. - ___1___ is a Beginner's 
Language: ___1___ is a great language for the beginner-level programmers and supports the ___6___ of a wide 
range of applications from simple text processing to WWW browsers to games."""

    hard_quiz_answer = ["Python", "interpreted", "English", "compile", "programming", "development"]

    very_hard_quiz_text = """___1___ Identifiers: A ___1___ identifier is a name used to identify a ___2___, 
function, class, module, or other object. An identifier starts with a ___5___ A to Z or a to z or an 
underscore (_) followed by zero or more ___5___s, ___7___, and digits (0 to 9). ___1___ does not allow 
___3___ characters such as @, $, and % within identifiers. ___1___ is a case sensitive ___4___ language.
Thus Manpower and manpower are two different identifiers in ___1___. Here are following identifier naming
convention for ___1___: - Class names start with an uppercase ___5___ and all other identifiers with a
lowercase ___5___. - Starting an identifier with a single leading underscore indicates by convention that
the identifier is  meant to be ___6___. - Starting an identifier with two leading ___7___ indicates a
strongly ___6___ identifier. - If the identifier also ends with two trailing ___7___, the identifier is a
language-defined special name."""

    very_hard_quiz_answer = ["Python", "variable", "punctuation", "programming", "letter", "private", "underscores"]

    ultra_hard_quiz_text = """Lines and Indentation: One of the first caveats programmers encounter when 
learning ___1___ is the fact that there are no ___2___ to indicate blocks of ___3___ for class and 
___4___ definitions or flow control. Blocks of ___3___ are denoted by line indentation, which is rigidly 
enforced. The number of ___5___ in the indentation is variable, but all statements within the block must 
be ___6___ the same amount. Multi-Line Statements: Statements in ___1___ typically end with a new line. 
___1___ does, however, allow the use of the line continuation character (\) to denote that the line should
continue. ___8___s in ___1___: A hash sign (#) that is not inside a ___7___ literal begins a ___8___.
All characters after the # and up to the physical line end are part of the ___8___, and the ___1___
interpreter ignores them."""

    ultra_hard_quiz_answer = ["Python", "braces", "code", "function", "spaces", "indented", "string", "comment"]

    return {"easy" : [easy_quiz_text, easy_quiz_answer], "medium" : [medium_quiz_text, medium_quiz_answer], "hard" : [hard_quiz_text, hard_quiz_answer], "very hard" : [very_hard_quiz_text, very_hard_quiz_answer], "ultra hard" : [ultra_hard_quiz_text, ultra_hard_quiz_answer]}

# Generate the quiz, containing the quiz text, quiz answer and the quiz blanks.
# Returnes quiz text, quiz answer and the quiz blanks. 
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

# Get the quiz text difficulty level from the user when game difficulty level is custom.
# Returnes a number representing the difficulty level.
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

# Checks if a word in quiz_blank is a substring of the word passed in.
def quiz_blank_in_pos(word, quiz_blank):
    if quiz_blank in word:
        return quiz_blank
    return None

# Replaces quiz_blank with user_quiz_answer
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

# Get the quiz answer from user.
def get_user_quiz_answer(quiz_blank, quiz_answer, number_of_guesses_left):

    while True:
        user_input = raw_input(os.linesep + "What should be substituted in for " + quiz_blank + "? ")

        if not user_input.lower() == quiz_answer.lower():
            number_of_guesses_left -= 1
            user_feedback_text = os.linesep * 2 + "That isn't the correct answer! You only have %s try left!" % (number_of_guesses_left)

            if number_of_guesses_left > 1:
                print user_feedback_text

            elif number_of_guesses_left == 1:
                print user_feedback_text + " Make it count!"

            else:
                break

        else:
            break

    return number_of_guesses_left

# When user have won the game.
def won(username):
    print os.linesep + "WOW Congratulations! " + username + ", you got all questions correct! :-D" + os.linesep

    if raw_input(username + " would you like to play again? (y/n) ").lower() == 'y': 
        game_loop(username) 
    else: 
        print username + ", thank you for playing, see you soon!" + os.linesep

# When the user have lost the game.
def game_over(username):
    print os.linesep + "Game Over!!! " + username + ", I am sorry! Better luck next time! :-)" + os.linesep

    if raw_input(username + " would you like to play again? (y/n) ").lower() == 'y': 
        game_loop(username) 
    else: 
        print username + ", thank you for playing, see you soon!" + os.linesep

    exit()

# This is the game loop that have the main responsibility to running the game.
def game_loop(username):
    number_of_guesses_left = None
    quiz_text= ""
    quiz_answers = []
    quiz_blanks = []

    difficulty_level = get_game_difficulty_level_from_user(username)

    number_of_guesses_left = get_number_of_guesses(difficulty_level)
    quiz_text, quiz_answers, quiz_blanks = get_quiz(difficulty_level, username, get_quiz_text_and_answer())
    
    print os.linesep + "You will get %s guesses per problem." % (number_of_guesses_left) + os.linesep
    
    print "The current paragraph reads as such:"
    print quiz_text

    quiz_text = quiz_text.split()

    count = 0
    for quiz_answer in quiz_answers:

        number_of_guesses_left = get_user_quiz_answer(quiz_blanks[count], quiz_answer, number_of_guesses_left)

        if number_of_guesses_left < 1:
            game_over(username)

        quiz_text = replace_word(quiz_text, quiz_blanks[count], quiz_answer)

        print os.linesep * 2 +  " ".join(quiz_text)

        count += 1

    won(username)

# This is to start the game.
def game():
    username = ""
    
    welcome()
    username = get_username_from_user()

    game_loop(username)

# This is the main method used for starting the program.
def main():
    game()


if __name__ == "__main__":
    main()