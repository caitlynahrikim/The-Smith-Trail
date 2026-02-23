# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 11:03:46 2024

@author: caitl
"""

""""Handles the main gameplay"""

from event_module import talbot_house, sessions_house, park_house, haven_house, paradise_pond, gate
import highscores_module
from player_health_module import player_health
import random
import display_module
import graphics
import sys



def start_game(win):
  '''
  This function handles all of the main gameplay.
  '''
  
  print("\nYour journey starts now. Stay safe!")
  player_name = input("\nWhat is your name? ")

  #create a list of events
  event_list = [
      lambda player_name: talbot_house (player_name, win), 
      lambda player_name: sessions_house (player_name, win), 
      lambda player_name: park_house (player_name, win), 
      lambda player_name: haven_house (player_name, win),
      lambda player_name: paradise_pond (player_name, win),
      lambda player_name: gate (player_name, win),
  ]

  #shuffle the list of functions
  random.shuffle(event_list)

  #Start the game with player_health logic 
  outcome, final_health = player_health(initial_health = 100, events=event_list, player_name = player_name)
  
  #highscores file 
  scores_file = "high_scores.txt"
  high_scores = highscores_module.read_high_scores(scores_file)

  #loop for outcome of the game win/lose when player health is <0 or >0
  if outcome == "lose":
      two_return = input("Press enter to continue ")
      if two_return == "":
          print(f"\nYou lose! {player_name}, your journey at Smith has ended. Better luck next time!")
          lose_image = graphics.Image(graphics.Point(display_module.WIDTH/2, display_module.HEIGHT/2), "lose.png")
          lose_image.draw(win)
          
          while True:
              print()
              repeat_game = input("Do you want to play again? Enter Y (yes) or N (no). ")
              if repeat_game == "Y":
                  win.close()
                  main()
              elif repeat_game == "N":
                  win.close() #close window
                  print()
                  print("Thank you for playing!")
                  sys.exit()
              else:
                  print()
                  print("Invalid input. Please enter Y or N. ")
                  continue
     

  else:
     two_return = input("Press enter to continue ")
     if two_return == "":
         print(f"\nCongratulations {player_name}, you survived The Smith Trail! You are now a Smithie!")
         win_image = graphics.Image(graphics.Point(display_module.WIDTH/2, display_module.HEIGHT/2), "win.png")
         win_image.draw(win)
         
        #Read the highscores 
         high_scores = highscores_module.read_high_scores(scores_file)

        #Add the player's name and score to high scores
         high_scores[player_name] = final_health

        #Save updated high scores to the file
         highscores_module.write_high_scores(scores_file, high_scores)
         
         while True:
             print()
             repeat_game = input("Do you want to play again? Enter Y (yes) or N (no). ")
             if repeat_game == "Y":
                 win.close()
                 main()
             elif repeat_game == "N":
                 win.close() #close window 
                 print()
                 print("Thank you for playing!")
                 sys.exit()
             else:
                 print()
                 print("Invalid input. Please enter Y or N. ")
                 continue
         
  return 



def view_high_scores(high_scores):
    """
    Displays the top 10 high scores.
    """
    print("\n--- Top 10 High Scores ---")
    # Sort the scores by value (health) in descending order
    sorted_scores = sorted(high_scores.items(), key=lambda x: x[1], reverse=True)[:10]

    if not sorted_scores:
        print("No high scores yet. Be the first to set one!")
    else:
        for rank, (name, score) in enumerate(sorted_scores, start=1):
            print(f"{rank}. {name}: {score}")

    input("\nPress enter to return to the main menu ")  # Pause for user input





def main():
  """
  Starts and runs game. Load images, runs main game loop, checks modules are working together properly, and handles exit of game.
  """

  # Initialize the game window once
  win = display_module.initialize_window()
 
  while True:
    #win = display_module.initialize_window()
    
   
    print("\n"*5)  
    print("""--------Welcome to The Smith Trail!--------
 
     You may:
 
      1. Travel the trail
      2. Learn about the trail
      3. See the Smith Top Ten
      4. End\n""")

    user_input = input("What is your choice? ")
    
    if user_input == "1":
        start_game(win)

    elif user_input == "2":
      #win.undraw()
      print("\nHere is information about the trail:\n"
          "\nA simpler remake of the Oregon Trail game but set at Smith College. Smith College was opened in 1875, and its dorm houses have been haunted many ghosts. The user will travel through Smith College, where they will attempt to survive ghostly encounters in various houses. The journey will be covering locations such as Talbot House, Sessions House, Park House, and Haynes House.\n\nLearn about the creators:"
          )
      # Clear the current window and display the creators image
      
      creators_image = graphics.Image(graphics.Point(display_module.WIDTH/2, display_module.HEIGHT/2), "creators.png")
      creators_image.draw(win)
      
      
      two_return = input("\nPress enter to return to menu ")
      if two_return == "":
          creators_image.undraw()  # Remove the image when returning to the menu
          #win.close()
          continue


    elif user_input == "3":
      #win.close()
      high_scores = highscores_module.read_high_scores("high_scores.txt")
      view_high_scores(high_scores)
      continue
  
    
    elif user_input == "4":
      print("\nThank you for playing!")
      win.close() #close window 
      sys.exit()
    
    
    else:
      print("Invalid choice. Please try again.")
      continue #goes back to menu prompt



if __name__ == "__main__":
  main()


