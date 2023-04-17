import random, os 
from graphic import hangman_graphic
from words import words


word = random.choice(words)
word = word.upper()
reveal = list(len(word)*'_')
lives = 6
win = False

def check_letter(letter,word):
	"""
	Checks if there is a letter given by the player in the word
	"""

	global reveal
	for i in range(0, len(word)):
		letter = word[i]
		if guess == letter:
			reveal[i] = guess
		if '_' not in reveal:
			return True
		else:
			return False	

def display_status():
	print(src.graphic.hangman_graphic[6 - lives])
	print(reveal)

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