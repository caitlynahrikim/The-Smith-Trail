# README for The Smith Trail

## Team Information
Team Members:  
- Caitlyn: Player Health/Main  
- Nazifa: Events/High scores/Display  
- Victoria: Graphics  

*All participated in debugging code

## Project Overview
The Smith Trail is a simpler remake of the Oregon Trail game, set at a haunted Smith College. Players navigate through various haunted houses on campus, attempting to survive ghostly encounters. The goal is to make it through all events while achieving the highest score.

---

## Files

## main.py
Handles the main gameplay logic and user interaction. Key responsibilities include:

- Starting the game and guiding the player through various events.
- Managing the main menu, including options to:
	- Start the game.
	- Learn about the trail.
	- View the top 10 high scores.
	- Exit the game.
- Shuffling and executing event sequences.
- Checking player health pts and determining win or loss outcome.
- Displaying high scores and allowing a replay option.

## event_module.py
Manages interactive scenarios within Smith campus. Key responsibilities include:

- Presenting players with themed locations and stories.
- Offering different choices that influence player outcomes.
- Updating visuals dynamically using the graphics library.
- Adjusting player's health pts or progress based on their choices.

	Features:

	- Dynamic Visuals: Each event uses the graphics library to display corresponding images for immersive gameplay.
	- Branching Choices: Players choose between two choices each with unique consequences affecting the player's health pts or progress.
	- Themed Locations: Six locations, each with different stories and choices (Talbot, Sessions, Park, Haven, Paradise Pond, Grecourt Gate).

## player_health_module.py
Manages the player's health score during the game. Key responsibilities include:

- Initializing the player's health points at the start of the game.
- Updating health points based on event outcomes.
- Determining the game outcome (win or lose) based on the player's final health points.
- Displaying the player’s current health points after each event.


## highscores_module.py
Manages the creation, reading, and writing of highscore files. Key responsibilities include:

- Reading high scores from a file while handling potential errors.
- Writing high scores back to the file in a sorted format.
- Ensuring error handling to maintain functionality even when files are missing or incorrectly formatted.

## display_module.py
Manages initialization and graphics setup for game using graphics library. Key responsibilities include:

- Creating and managing the game window.
- Setting up the coordinate system for graphic elements.
- Displaying the game’s logo at start of game

## graphics.py
Code in graphics library which allowed us to create our game window, logo, location images, and win/lose endings.

## high_scores.txt
A file that stores top 10 scoring players' names and scores.

## images stored in graphics folder

## flow-diagram of final game uploaded as a png

---

## How to Run and Interact with the Game

1. Setup:
   - Ensure all required files are in the `final_project` directory and all images have been downloaded.
   - Run `main.py` to start the game.
   - Move console to the left half of screen and game window to the right.

2. Game Menu:
   - Upon starting, you'll see the following menu:
     ```
     --------Welcome to The Smith Trail!--------

     You may:

     1. Travel the trail
     2. Learn about the trail
     3. See the Smith top ten
     4. End
     ```
   - Enter a number (1-4) to select an option
     
3. Playing the Game:
   - Enter your name
   - Progress through events visiting each house. 
   - Monitor your health, displayed in the console after each event.
   - Complete all events to win, or lose if your health reaches zero.

4. High Scores:
   - After finishing the game, your score is calculated based on your final health points.
   - Scores are updated and saved automatically.

5. Exiting the Game:
   - Ends the game and takes your score. 
