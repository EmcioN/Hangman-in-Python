import random, os 
from src.graphic import hangman_graphic
from src.words import words



def hangman_game():
	"""
	Run the hangman game
	"""	
	word = random.choice(words)
	word = word.upper()
	reveal = ["_" for i in range(len(word))]
	lives = 6
	win = False
	used_letters = []

	def check_letter(letter,word):
		"""
		Checks if there is a letter given by the player in the word
		"""
		
		for i in range(len(word)):
			if letter == word[i]:
				reveal[i] = letter					
			if '_' not in reveal:
				return True				
		else:			
			return False				

	def display_status():
		"""
		Show hangman graphic, how many lives you have and word to reveal
		"""	
		os.system("clear")	
		print(hangman_graphic[6 - lives])
		print(" ".join(reveal))
		print('Your lives',lives)
		print('Used letters:', ' '.join(used_letters))
		
		
	while win == False and lives > 0:
		display_status()
		guess = input('Guess a letter or an entire word:')
		guess = guess.upper()
		if guess == word:
			win = True
			reveal = word			
		elif len(guess) == 1 and guess in word:			
			win = check_letter(guess,word)			
		else:			
			lives -= 1
			used_letters.append(guess)			
		if guess not in used_letters:
			used_letters.append(guess)				
		display_status()
	if win:
		print('---------------------------------------')
		print('Congratulations you saved the hangman!!')
		print('---------------------------------------')
	else:
		print('--------------------------------------------------------------')
		print('This time you failed to save the hangman. The word was:',word)
		print('--------------------------------------------------------------')  

name = input('What is your name ?')

print("   _    _")
print("  | |  | |")
print("  | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __")
print("  |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \\")
print("  | |  | | (_| | | | | (_| | | | | | | (_| | | | |")
print("  |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|")
print("                       __/ |")
print("                      |___/")
print("  -----^")
print("  |    |")
print(" x_x   |")
print(" /|\   |")
print(" / \   |")
print("       |")
print("-------o")
print('Welcome to HANGMAN',name,'!!')
print('-------------------------------')
print('The rules are simple. Try to guess the word before you hang our poor dude. Guess the letters or guess the whole word')

play_game = input("Would you like to start the game? (y/n) ")

if play_game.lower() == "y":
    print("Let's play the game!")
    hangman_game()
elif play_game.lower() == "n":
    print("Okay, see you next time!")	
else:
    print("I don't understand, can you repeat?")

play_again = input("Would you like to play again? (y/n) ")

while True:
    if play_again.lower() == "y":
        print("Let's play the game!")
        hangman_game()
        play_again = input("Would you like to play again? (y/n) ")
    elif play_again.lower() == "n":
        print("Thanks for playing! Goodbye!")
        break
    else:
        play_again = input("I don't understand, please enter y or n: ")