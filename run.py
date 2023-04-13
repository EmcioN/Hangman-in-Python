import gspread
from google.oauth2.service_account import Credentials
import random

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Hangman') 
highscore = SHEET.worksheet("highscore")

data = highscore.get_all_values()   import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Hangman') 
highscore = SHEET.worksheet("highscore")

data = highscore.get_all_values()   

#Words

words =["beetle", "satiate", "thread", "protective", "tasteless",
 "conduct","elastic", "satisfy", "sweater", "insurance", "marvelous"]

def pick_word():
    """
    Get a random word from the words list
    """
    random_word = random.choice(words)
    return random_word.upper()

# Hangman graphics 

def hangman_graphic(self, guesses):
		if guesses == 0:
			print "________      "
			print "|      |      "
			print "|             "
			print "|             "
			print "|             "
			print "|             "
		elif guesses == 1:
			print "________      "
			print "|      |      "
			print "|      0      "
			print "|             "
			print "|             "
			print "|             "
		elif guesses == 2:
			print "________      "
			print "|      |      "
			print "|      0      "
			print "|     /       "
			print "|             "
			print "|             "
		elif guesses == 3:
			print "________      "
			print "|      |      "
			print "|      0      "
			print "|     /|      "
			print "|             "
			print "|             "
		elif guesses == 4:
			print "________      "
			print "|      |      "
			print "|      0      "
			print "|     /|\     "
			print "|             "
			print "|             "
		elif guesses == 5:
			print "________      "
			print "|      |      "
			print "|      0      "
			print "|     /|\     "
			print "|     /       "
			print "|             "
		else:
			print "________      "
			print "|      |      "
			print "|      0      "
			print "|     /|\     "
			print "|     / \     "
			print "|             "
			print "Oh no.. You didn't save the Hangman"			
			print "GAME OVER!"
	