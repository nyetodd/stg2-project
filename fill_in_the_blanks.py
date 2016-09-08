# IPND Stage 2 Final Project

# paragraphs taken from Python wikipedia page: https://en.wikipedia.org/wiki/Python_(programming_language)

all_paragraphs = ['''An important goal of ___1___'s developers is making it ___2___ to use. This is reflected in the origin of the name,
 which comes from Monty ___1___, and in an occasionally playful approach to tutorials and reference materials, such as using 
 examples that refer to spam and ___3___ instead of the standard ___4___ and bar. ''', 

'''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions.''', 

'''Python ___1___s are available for many operating ___2___, allowing Python code to run on a wide variety 
of ___2___. Using third-party tools, such as Py2exe or Pyinstaller, Python code can be ___3___ into stand-alone 
___4___ programs for some of the most popular operating ___2___, so Python-based software can be distributed to, 
and used on, those environments with no need to ___5___ a Python ___1___.''']

all_answers = [["Python", "fun", "eggs", "foo"],["function", "parameters", "None", "list"],["interpreter", "systems", "packaged", "excecutable", "install"]]

all_blanks = [['___1___', '___2___', '___3___', '___4___' ], ['___1___', '___2___', '___3___', '___4___' ], ['___1___', '___2___', '___3___', '___4___', '___5___']]

levels = ['EASY', 'MEDIUM', 'HARD']

def main():
	''' Main function for game - level is set and then play triggered'''
	play = True
	while play == True:
		welcome_message()
		level_index = set_level_index(get_level_from_user)
		total_guesses = set_guesses()
		play_level(all_paragraphs[level_index], all_answers[level_index], all_blanks[level_index], total_guesses)
		play = play_again()
	print "Thanks for playing!"

def welcome_message():
	''' Prints welcome message for user '''
	print "--------------------------------------"
	print
	print "Welcome to the fill in the blanks game!"
	print 
	print "Your challege, should you wish to accept it, is to correctly identify the missing words in the paragraph you are shown."
	print 

def set_level_index(input_func):
	''' takes in an input method to allow method to be tested. Returns the index of the specified level 
	in the levels list, which allows the correct paragraph, answers and blanks to be provided to the 
	main game method. Input function is passed in to allow user input to be mocked in unittests'''
	print "There are three difficulty levels, EASY, MEDIUM or HARD."
	print
	level = input_func()
	print "Great! You've selected " + level + "!"
	print
	return levels.index(level)

def set_guesses():
	'''allows the user to set the total_guesses variable and checks whether int or long before returning'''
	total_guesses = input('You can have up to 20 guesses - how many would you like?:')
	while is_valid_total_guesses(total_guesses) != True:
		total_guesses = input('Invalid input. Please enter a number from 1 to 20:')
	print "Okay, you'll get " + str(total_guesses) + " guesses to fill in all the blanks."
	return total_guesses

def is_valid_total_guesses(total_guesses):
	''' helper method - takes number of guesses and checks that it is valid (int or long between 0 and 20. Returns 
	True if valid and False if not'''
	if isinstance(total_guesses, (int, long, float)) != True:
		return False
	elif (0 < total_guesses <= 20) != True:
		return False
	else: 
		return True

def play_level(paragraph, answer_list, blanks, total_guesses):
	''' takes the paragraph, answer_list and blanks for the selected level and accepts
	guesses until guesses are all used or all blank spaces are filled'''
	guesses_left = total_guesses
	num_of_blanks = len(blanks)
	print
	print paragraph
	while guesses_left > 0 and num_of_blanks > 0:
		for answer in answer_list:
			print answer
			while guesses_left > 0:
				blank_number = answer_list.index(answer)
				guess = get_guess_from_user(blank_number, blanks)
				if check_guess(guess, answer) == True: 
					paragraph = update_paragraph(paragraph, answer, answer_list, blanks)
					num_of_blanks = num_of_blanks - 1
					success_message(guess, guesses_left, total_guesses, num_of_blanks, paragraph)
					break
				else: 
					guesses_left = guesses_left - 1
					wrong_guess_message(guess, guesses_left, paragraph)
	return 

def play_again():
	''' Returns whether the user wants to play another round'''
	accepted_responses = ["YES", "No"]
	play_response = (raw_input("Would you like to play again? (Y/N):")).upper()
	if play_response in accepted_responses[0]:
		return True
	else:
		return False

def get_level_from_user():
	''' Helper method that prompts the user for the level that they want and checks it is valid. Split
	out so that this method can be mocked in unit tests'''
	print
	level = str(raw_input('Which would you like to play?:'))
	while is_valid_level(level) != True:
		print
		level = str(raw_input('Which would you like to play?:'))
	return level.upper()

def get_guess_from_user(blank_number, blanks):
	''' Takes in current answer being guessed and prompts user to guess that blank. Returns guess in string format'''
	current_blank = blanks[blank_number]
	print 
	guess = raw_input('Guess what should be in place of ' + current_blank + ':')
	return str(guess)

def is_valid_level(user_input):
	''' Helper method - takes in input from user and checks that it is a valid level. Returns true
	if it is and false otherwise.'''
	user_input = str(user_input).upper()
	if user_input in levels:
		return True
	else: 
		print
		print "Sorry, that's not one of the options. The difficulty levels are: EASY, MEDIUM or HARD"
		return False			

def check_guess(guess, answer):
	''' Takes the current answer being checked against and the user's guess and 
	returns True if the guess is a substring of the answer and False if not. User
	input is converted to lowercase for a better match '''
	if answer.lower() in guess.lower(): 
		return True
	else:
		return False 

def update_paragraph(paragraph, answer, answer_list, blanks):
	''' Takes current paragraph, answer, answer_list and blanks and returns paragraph 
	updated to replace correctly guessed blank with its answer and correctly capitaized'''
	blank = blanks[answer_list.index(answer)] 
	paragraph = paragraph.replace(blank, answer)
	return capitalize_sentences(paragraph)

def capitalize_sentences(paragraph):
	''' Helper function for update paragraph. Takes paragraph and returns same paragraph 
	with first word in sentence properly capitalized'''
	sentences = paragraph.split('.')
	replaced = []
	for sentence in sentences:
		words = sentence.split()
		if len(words) != 0:
			words[0] = words[0].capitalize()
		sentence = ' '.join(words)
		replaced.append(sentence)
	capitalized_paragraph = ('. '.join(replaced)).strip(' ')
	return capitalized_paragraph

def wrong_guess_message(guess, guesses_left, paragraph):
	''' prints messages related to an unsuccessful guess, based on remaining guesses '''
	print
	if guesses_left == 0:
		print "Sorry, the blank isn't " + guess + " and you have no more guesses left. Game over :("
	elif guesses_left == 1: 
		print "Oh no, the blank isn't " + guess + ". Try again, you have " + str(guesses_left) + " guess left!"
	else:
		print "Oh no, the blank isn't " + guess + ". Try again, you have " + str(guesses_left) + " guesses left!"
	print
	print "The current paragraph is:"
	print paragraph

def success_message(guess, guesses_left, total_guesses, num_of_blanks, paragraph):
	''' prints messages related to a successful guess, based on remaining guesses and whether level completed'''
	print
	print "Success! " + guess + " is correct!"
	if num_of_blanks == 0:
		if guesses_left == 1: 
			print "Phew, that was close! You've filled in all the blanks with " + str(guesses_left) + " guess left!"
		elif guesses_left == total_guesses:
			print "Wow, you're good! You filled in all the blanks without using up any of your guesses!"
		else:
			print "Well done! You've filled in all the blanks with " + str(guesses_left) + " guesses left!"
	print 
	print "The updated paragraph is:"
	print paragraph

main()
	
