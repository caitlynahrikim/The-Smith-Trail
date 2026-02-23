# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 15:36:46 2024

@author: caitl
"""

"""
Updates player’s health percentage based on each decision they make in each house event. Imports point system from event_module.
"""

from event_module import talbot_house, sessions_house, park_house, haven_house, paradise_pond, gate


#list of events to occur in game
event_list = [talbot_house, sessions_house, park_house, haven_house, paradise_pond, gate]

def player_health(initial_health = 100, events=[], player_name = "Enter"):
    """
    manages player's health throughout game, updating it based on events, and determining game's outcome
    
    Parameters:
        initial_health (int): starting health of player. default is 100%
        events (list of functions): list of event functions that update health
    
    Return:
        str: message indicating if player wins or loses
    """
    # set player's health to start value
    health = initial_health
    
    # loop through each event in game
    for event in events:
        # call event function and set it equal to health change value
        health_change = event(player_name) # event functions return health adjustments
        
        # apply health change to health var
        health += health_change
        # make sure health percentage is displayed (update percent display)
        print()
        print(f"Health Points: {health}") #would be in top right corner of screen
        print("-" * 30)
        
        # if health becomes 0 or below, player dies
        if health <= 0:
            print()
            print("*" * 30)
            return "lose", 0  #used to determine if player would be put on leaderboard
    
    # if loop ends and health is above zero, player survives
    print()
    print("*" * 30)
    return "win", health  #used to determine if player would be put on leaderboard




