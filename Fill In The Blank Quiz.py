easy = "Michael ___1___ played for the Chicago ___2___.  Casius Clay changed his name to Muhammad ___3___.  Barack ___4___ was the 44th President of the United States."  
 
answer_easy = ["jordan", "bulls", "ali", "obama"]
   
medium = "A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary, tuple, and ___4___ or can be more complicated such as objects and lambda functions.\n"
 
answer_medium = ["function", "variables", "none", "list"]
 
hard = "The ___1___ was invented in the early 1990s. The World Wide Web is made up of HTML ___2___ and is the language ___3___ use to interpret web pages. ___4___ stands for Hypertext Markup Language. " #is this provided somwhere?#
 
answer_hard = ["world wide web", "documents", "browsers", "html"]
 
answers = [answer_easy, answer_medium, answer_hard]
 
paragraphs = [easy, medium, hard]

greeting = "WELCOME TO CARARRUS' FILL IN THE BLANK QUIZ\n"

blanks = ["___1___", "___2___", "___3___", "___4___"]
 
def choose_level():
  """choose the difficulty level"""
  #Inputs:  Difficulty level
  #Outputs:  paragraph in relation to difficulty level
  answer = False
  while answer == False:
    game_level = raw_input("Please enter a difficulty level. Easy, medium or hard?\n")
    print "You've chosen " + str(game_level) + ".\n"
    if game_level == "easy":
      answer = True
      level = 0
    elif game_level == "medium":
      answer = True
      level = 1
    elif game_level == "hard":
      answer = True
      level = 2
    else:
      print "Error:  Please choose the easy, medium, or hard."
      answer = False    
  return level
 
def determine_attempts():
  """prompts user to determine how many attempts"""
  #Inputs:  # of attempts requested by user
  #Outputs:  game gives number of attempts user selected before ending 
  how_many_tries = int(raw_input("How many attempts do you want to answer a blank correctly before the answer is provided to you? Please provide a number, such as 2.\n"))
  attempts = how_many_tries
  number_of_tries = 5
  while how_many_tries < 1:
    print "Please try again."
    determine_attempts
    attempts = attempts + 1
    if attempts == number_of_tries:
      break 
  else:
    print "Please read the paragraph below and provide the answers to fill in the numbered blanks.\nYou will be given " + str(attempts) + " chances to enter the correct answer before it is provided to you.\n"
    return how_many_tries

def display_filled_paragraph(level, position):
  #Inputs:  User inputs correct answer of question
  #Outputs:  Displays the sentence as the user fills it in
  replacement_position = 1
  paragraph = paragraphs
  while replacement_position <= position:
    paragraphs[level] = paragraphs[level].replace(blanks[replacement_position-1], answers[level][replacement_position-1])
    replacement_position += 1
  print(paragraphs[level])
 
# Runs the quizzes and outputs the following given guesses  
def quiz(level, attempts):  
  print "Begin the quiz:\n" + str(paragraphs[level])
  guesses = 1
  while guesses <= attempts: # removed attempts = 5
    response = raw_input("\nWhat is answer " + str(guesses) + "?\n").lower()
    if response == answers[level][guesses - 1]:
      correct("You are correct!\n", level, guesses) 
      guesses = guesses + 1
    else:
      while response != answers[level][guesses-1]:
        print "Please try again\n"
        response = raw_input("What is answer " + str(guesses) + "?\n").lower()
        if response == answers[level][guesses - 1]:
          correct("You are correct!\n", level, guesses)
        elif guesses > attempts:
          print "The correct answer is " + str(answers[level][guesses-1])
          response = answers[level][guesses-1]
        guesses = guesses + 1 # changed indentation here so that it's actually incrementing in while loop

def correct(message, level, guesses):
   print message
   display_filled_paragraph(level, guesses)
   return
 
def play_game():
  #Input:
      #user inputs level of game and number of attempts desired
  #Behavior:
      #Game runs the quiz based on level and number attempts user chooses.
      #It checks the users input, if correct it replaces blank with correct answer.
      #If wrong it asks the user to please try again.
      #This continues until the user has exhausted number of attempts chosen or answers all questions correctly.
  #Output:
      #None
  print greeting
  quiz(choose_level(), determine_attempts())
  
#start program
print play_game()
print "Congratulations! You have filled in all the blanks correctly.\n"
raw_input("Press the enter key to exit.")
