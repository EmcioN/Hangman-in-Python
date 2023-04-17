import random, os 
from src.graphic import hangman_graphic
from src.words import words



def hangman_game():
	"""
	Run the hangman game
	"""	
	word = random.choice(words)
	word = word.upper()
	reveal = list(len(word)*'_')
	lives = 6
	win = False

	def check_letter(letter,word):
		"""
		Checks if there is a letter given by the player in the word
		
		"""
				
		for i in range(0, len(word)):
			letter = word[i]
			if guess == letter:
				reveal[i] = guess
			if '_' not in reveal:
				return True
			else:
				return False	

	def display_status():
		"""
		Show hangman graphic, how many lives you have and word to reveal
		"""		
		print(hangman_graphic[6 - lives])
		print(reveal)
		print('Your lives',lives)

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
		display_status()
	if win:
		print('Congratulations you saved the hangman!!')
	else:
		print('This time you failed to save the hangman. The word was:',word)  

name = input('What is your name ?')
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