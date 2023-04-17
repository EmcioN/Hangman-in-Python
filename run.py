import random, os 
from src.graphic import hangman_graphic
from src.words import words


reveal = list(len(words)*'_')
lives = 6
win = False

def check_letter(letter,words):
	"""
	Checks if there is a letter given by the player in the word
	"""
	
	global reveal
	for i in range(0, len(words)):
		letter = words[i]
		if guess == letter:
			reveal[i] = guess
		if '_' not in reveal:
			return True
		else:
			return False	

while win == False and lives > 0:
	print(reveal)
	guess = input('Guess a letter or an entire word:')
	guess = guess.upper()

	if guess == words:
      win = True
      reveal = words
	if len(guess) == 1 and guess in words:
			
   
    else:
      lives -= 1
  
if win:
  print('Congratulations you saved the hangman!!')
else:
  print('This time you failed to save the hangman. The word was:',words)  