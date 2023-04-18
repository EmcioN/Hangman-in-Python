![logo](/doc/images/logo.png)


## Table of Contents
[UX](#ux)
  * [Goal for the Project](#goal-for-the-project)
  * [User Goals](#user-goals)
  * [User Stories](#user-stories)
  * [Site owner Goals](#site-owner-goals)    
  * [Design Choices](#design-choices)    
    * [Colours](#colours)    
  * [Features](#features)
    * [Name](#name)
    * [Start Game](#start-game)    
    * [Stage](#stage)
    * [End Game](#end-game)      
  * [Tehnologies used](#tehnologies-used)
    * [Languages](#languages)
    * [Tools](#tools)
  * [Testing](#testing)
  * [Deployment](#deployment)
  * [Credits](#credits)

## UX
## Goal for the Project
 This is a classic Hangman game implemented in Python. You can play the game in the browser. The game features graphics and colors that are implemented in Python.
## User Goals
  * The user wants to play a game of Hangman.
  * The user wants to see graphic of the hangman. 
  * The user wants to be able to play the game in the browser.
## User Stories
  * As a user, I want to be able to start a new game.
  * As a user, I want to see the number of letters in the word I need to guess.
  * As a user, I want to see how many guesses I have left.
  * As a user, I want to be able to guess a letter.
  * As a user, I want to see if the letter I guessed is correct or not.
  * As a user, I want to see the letters I have guessed so far.
  * As a user, I want to see if I have won or lost the game.
## Site owner Goals
  * To create an engaging and entertaining game for users.
  * To implement the game using Python.
  * To use graphics and colors to enhance the user experience.
  * To provide a user-friendly interface for the game.
## Design Choices
  * The game's design is kept minimalistic to maintain focus on the gameplay.
### Colours   
  * The colours in the game are supplied by the Python Colorama Model
## Features
### Name 
 The player will be able to choose his name.

![name](/doc/images/name-input.png)

### Start Game
 The player will be able to choose whether he wants to start a new game or finish the game. Just type "y" to start or "n" to stop

![play](/doc/images/start-game.png)

### Rules
 Quick and short rules for reference
 
 ![rules](/doc/images/rules.png)

### Stage
 The player will see a graphic that will tell him how many mistakes he can still make. With each level, lines will be added until the hangman character is drawn. When we see the whole character, we lose the game. Guess the word faster to save the poor guy.
  * Stage 1

  ![start](/doc/images/stage1.png)

  * Stage 2

  ![stage2](/doc/images/stage2.png)

  * Stage 3

  ![stage3](/doc/images/stage3.png)

  * Stage 4

  ![stage4](/doc/images/stage4.png)

  * Stage 5

  ![stage5](/doc/images/stage5.png)

  * Stage 6

  ![stage6](/doc/images/stage6.png)

  * Stage 7 

  ![stage7](/doc/images/stage7.png)

### End Game
 The contestant will see here whether he won or lost. He will also have the option to start a new game or end the program. The choice will be as simple as before. Simply type "y" or "n" to continue 

![end-game](/doc/images/end-game.png)

![end-game](/doc/images/end-game-win.png)

## Tehnologies used
### Languages Used 
* [Python](https://www.python.org/) - Used to create the project
### Tools
* [Github](https://github.com/) - Used to store the project
* [Codeanywhere](https://app.codeanywhere.com/) - Used to build the project
* [Heroku](https://id.heroku.com)- Used to deploy the project
* [Visual Studio](https://code.visualstudio.com/)- Used to create most of README file
## Testing

## Deployment
 * Log in to Heroku or create a new account.
 * Click the New button in the top right corner and select Create New App.
 * Choose a unique name for your app and select the region you want it to run in, then click Create App.
 * Go to the Deploy tab and click on the Settings tab.
 * Scroll down to Config Vars and click Reveal Config Vars.
 * Add a key called "port" with a value of "8000" and click Add.
 * Add another key called "CREDS" with your Google credentials as the value, and click Add again.
 * Scroll down to the Buildpack section and click Add Buildpack.
 * Select "python" and click Save Changes.
 * Repeat step 8 and add "node.js" as well.
 * Make sure the Buildpacks are in the correct order by clicking and dragging them if necessary.
 * Go back to the top of the page and select the Deploy tab again.
 * Choose Github as the deployment method and confirm that you want to connect to your Github account.
 * Search for your repository name and click the connect button.
 * Scroll to the bottom of the deploy page and select your preferred deployment type.
 * You can choose to enable automatic deploys for automatic deployment when you push updates to Github.
 * That's it, your site should now be deployed!

### Forking 
 * Open GitHub
 * Click on the project to be forked
 * Find the Fork button at the top right of the page
 * Once you click the button the fork will be in your repository

### Cloning
 * Open GitHub and locate the repository you want to clone.
 * Click on the "Clone or download" button.
 * Copy the URL provided.
 * Open a terminal or command prompt on your computer.
 * Navigate to the directory where you want to clone the repository.
 * Enter the following command:

 git clone [paste the URL you copied]
 
 * Press Enter.
 * Wait for the repository to finish cloning.
 * Once the cloning process is complete, you should see a message confirming the successful clone. 
## Credits
[Stackoverflow](https://stackoverflow.com/) was also very helpful. There you can find a solution with an explanation to most problems.

[W3school](https://www.w3schools.com/) is another place where I was looking for information. Everything is nicely explained and you can test it yourself.

Of course, the greatest support I received was from my mentor. Many thanks to him.

[Simen Daehlin](https://github.com/Eventyret)