# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 16:40:08 2024

@author: caitl
"""
import graphics
import display_module



def talbot_house(player_name, win):

    '''
    This function sets the background as the house, gives an initial
    scenario, give the user 2 places they can go and gives them another scenario
    based on their choice
    '''

    #set background as image
    #print initial scenario and 2 choices
    #if loop based  on choice selected
    #print error if they pick choice 1 or 2 then ask for input again
    
    
    print()
    player_enter = input("Press enter to continue ")
    if player_enter == "":
        talbot_image = graphics.Image(graphics.Point(display_module.WIDTH/2, display_module.HEIGHT/2), "talbot.png")
        talbot_image.draw(win)
    
        print()
        print("~~~~~~~~~~TALBOT HOUSE~~~~~~~~~~")
        print(player_name, "you stumble into Talbot house looking for the bathroom but then all of a sudden you hear crying… a little boy crying. What do you do?")
        print()
        print("1. Go to the attic ")
        print("2. Go through the red door")
        print()
    
        
    
        while True:
            choice = input("What is your choice? ")
            print()
    
            if choice == "1":
                talbot_attic_image = graphics.Image(graphics.Point(display_module.WIDTH/2, display_module.HEIGHT/2), "talbot_1.png")
                talbot_attic_image.draw(win)
                print("-" * 30) 
                print("You see a pale, sickly looking little boy curled up in the corner with his head down. His name is Thomas, he’s been locked in the attic for 100 years. He sees you and starts throwing a tantrum… oh no", player_name, "you angered the boy. He attacks you!")
                return -15
    
            elif choice == "2":
                outside_image = graphics.Image(graphics.Point(display_module.WIDTH/2, display_module.HEIGHT/2), "outside.png")
                outside_image.draw(win)
                print("-" * 30)
                print("Good choice", player_name, "you have left Talbot house in one piece!")
                return 0
    
            else:
                print("Error you must choose 1 or 2")
                continue    
    
        return talbot_house
    
    

def sessions_house(player_name, win):
    '''
    This function sets the background as the house, gives an initial
    scenario, gives the user 2 places they can go and gives them another scenario
    based on their choice
    '''

   #set background as image
   #print initial scenario and 2 choices
   #if loop based  on choice selected
   #print error if they pick choice 1 or 2 then ask for input again
    
    
    print()
    player_enter = input("Press enter to continue ")
    if player_enter == "":
        sessions_image = graphics.Image(graphics.Point(display_module.WIDTH/2, display_module.HEIGHT/2), "sessions.png")
        sessions_image.draw(win)
        print() #start it a bit lower
        print("~~~~~~~~~~SESSIONS HOUSE~~~~~~~~~~")
        print(player_name, "as you explore Smith College, your curiosity gets the best of you. You walk straight into Sessions, the oldest house on campus. Two shadowy figures run past you into the staircase. What do you do?")
        print()
        print("1. Follow them into the stairway")
        print("2. Go to the living room")
        print()
    
        global player_health
    
        while True:
            choice = input("What is your choice? ")
            print()
    
            if choice == "1":
                sessions_stair_image = graphics.Image(graphics.Point(display_module.WIDTH/2, display_module.HEIGHT/2), "sessions_1.png")
                sessions_stair_image.draw(win)
                print("-" * 30)
                print("Can they get a room? John, a man in a British army uniform from the 1700s, is holding hands with his lieutenant's daughter Lucy! The couple giggle at the top of the stairs but then they notice you watching them. They’re no longer laughing, they scream and run towards you, pushing you down the stairs!")
                return -20
    
            elif choice == "2":
                livingroom_image = graphics.Image(graphics.Point(display_module.WIDTH/2, display_module.HEIGHT/2), "sessions_2.png")
                livingroom_image.draw(win)
                print("-" * 30)
                print("Good choice", player_name,"you have left Sessions house in one piece!")
                return +15
    
            else:
                print("Error you must choose 1 or 2")
                continue
    
        return sessions_house



def park_house(player_name, win):
    '''
    This function sets the background as the house, gives an initial
    scenario, gives the user 2 places they can go and gives them another scenario
    based on their choice
    '''
    #set background as image
    #print initial scenario and 2 choices
    #if loop based  on choice selected
    #print error if they pick choice 1 or 2 then ask for input again
    
    
    print()
    player_enter = input("Press enter to continue ")
    if player_enter == "":
        park_image = graphics.Image(graphics.Point(display_module.WIDTH/2, display_module.HEIGHT/2), "park.png")
        park_image.draw(win)
        print()
        print("~~~~~~~~~~PARK HOUSE~~~~~~~~~~")
        print("Smoke comes out of a house, it looks a bit burnt but", player_name, "you are fearless and walk in. Inside the lights are gone and your eyes and throat burns a little from the smoke. In the distance you see someone laying on the floor, who is that?")
        print()
        print("1. Go to the kitchen")
        print("2. Walk through the hallway")
        print()
    
        global player_health
        #global player_name
    
        while True:
            choice = input("What is your choice? ")
            print()
    
            if choice == "1":
                kitchen_image = graphics.Image(graphics.Point(display_module.WIDTH/2, display_module.HEIGHT/2), "park_1.png")
                kitchen_image.draw(win)
                print("-" * 30)
                print("A lady, Jeanne, dressed in an apron lays on her side. A match in her hand that has not been lit yet. Suddenly she jumps up, runs the match against the floor lighting a fire and throws it on the ground. She closes the kitchen door and runs away.", player_name, "you are now stuck in the middle of a fire!")
                return -60
    
            elif choice == "2":
                hallway_image = graphics.Image(graphics.Point(display_module.WIDTH/2, display_module.HEIGHT/2), "park_2.png")
                hallway_image.draw(win)
                print("-" * 30)
                print("Bad decision " + player_name + ", why would you walk through a smokey house? You cough your entire way through the hallway to the exit. Where you finally get some fresh air.")
                return -5
    
            else:
                print("Error you must choose 1 or 2")
                continue
    
        #print("\nhealth = ", player_health)
    
        return park_house



def haven_house(player_name, win):
    '''
    This function sets the background as the house, gives an initial
    scenario, gives the user 2 places they can go and gives them another scenario
    based on their choice
    '''
    #set background as image
    #print initial scenario and 2 choices
    #if loop based  on choice selected
    #print error if they pick choice 1 or 2 then ask for input again
    
    
    print()
    player_enter = input("Press enter to continue ")
    if player_enter == "":
        haven_image = graphics.Image(graphics.Point(display_module.WIDTH/2, display_module.HEIGHT/2), "haven.png")
        haven_image.draw(win)
        print()
        print("~~~~~~~~~~HAVEN HOUSE~~~~~~~~~~")
        print("Sylvie…sylvie…sylvie. Sylvia Plath, the most famous alum, class of 1955 still lives in Haven house.", player_name, "you’re excited, you finally get to meet her or what she is now… where do you go?")
        print()
        print("1. Go to the basement")
        print("2. Walk through the hallway")
        print()
    
    
        while True:
            choice = input("What is your choice? ")
            print()
    
            if choice == "1":
                haven_basement_image = graphics.Image(graphics.Point(display_module.WIDTH/2, display_module.HEIGHT/2), "haven_2.png")
                haven_basement_image.draw(win)
                print("-" * 30)
                print("You discover Smithies having a party dancing to some fun and groovy Halloween music and invite you to dance with them! You receive king-sized candy bars and some new song recommendations.")
                return +30
    
            elif choice == "2":
                haven_hallway_image = graphics.Image(graphics.Point(display_module.WIDTH/2, display_module.HEIGHT/2), "haven_1.png")
                haven_hallway_image.draw(win)
                print("-" * 30)
                print("She is roaming around the hallway passing by student rooms, whispering about finding the meaning of life and you disrupt her flow! She looks at you upset, approaches you, and kindly asks you to leave the area.")
                return 0
    
            else:
                print("Error you must choose 1 or 2")
                continue
    
        return haven_house


def paradise_pond(player_name, win):
    '''
    This function sets the background as the pond, gives an initial
    scenario, gives the user 2 places they can go and gives them another scenario
    based on their choice
    '''
    #set background as image
    #print initial scenario and 2 choices
    #if loop based  on choice selected
    #print error if they pick choice 1 or 2 then ask for input again
   
    
    print()
    player_enter = input("Press enter to continue ")
    if player_enter == "":
        pond_image = graphics.Image(graphics.Point(display_module.WIDTH/2, display_module.HEIGHT/2), "pond.png")
        pond_image.draw(win)
        print()
        print("~~~~~~~~~~PARADISE POND~~~~~~~~~~")
        print("Finally you're not stuck inside some old wooden house. Paradise pond is huge and reflects the beautiful sky. The birds are chirping, the trees sway with the wind. There are two activities available for you to do at the pond. What do you want to do?")
        print()
        print("1. Walk along the boathouse dock")
        print("2. Walk along Mill River trail")
        print()
    
    
        while True:
            choice = input("What is your choice? ")
            print()
    
            if choice == "1":
                boathouse_image = graphics.Image(graphics.Point(display_module.WIDTH/2, display_module.HEIGHT/2), "dock.png")
                boathouse_image.draw(win)
                print("-" * 30)
                print("You walk onto the boathouse dock and gaze at the geese swimming in the lake when someone suddenly pushes you and you fall into the pond! Luckily, nearby Smithies pull you out of the water but the culprit could not be found…")
                return -30
    
            elif choice == "2":
                mill_image = graphics.Image(graphics.Point(display_module.WIDTH/2, display_module.HEIGHT/2), "mill.png")
                mill_image.draw(win)
                print("-" * 30)
                print("Good choice " + player_name + "! You have a nice view of Paradise Pond watching Smithies in a rowing race before exploring the gorgeous fall-colored forest behind Smith. What a nice way to relax.")
                return +35
    
            else:
                print("Error you must choose 1 or 2")
                continue
        
        return paradise_pond
    
    

def gate(player_name, win):
    '''
    This function sets the background as the gate, gives an initial
    scenario, gives the user 2 places they can go and gives them another scenario
    based on their choice
    '''
    #set background as image
    #print initial scenario and 2 choices
    #if loop based  on choice selected
    #print error if they pick choice 1 or 2 then ask for input again
    
    
    print()
    player_enter = input("Press enter to continue ")
    if player_enter == "":
        gate_image = graphics.Image(graphics.Point(display_module.WIDTH/2, display_module.HEIGHT/2), "gate.png")
        gate_image.draw(win)
        print()
        print("~~~~~~~~~~GRÉCOURT GATE~~~~~~~~~~")
        print("The big black grécourt gates are open right in front of college hall, looming over your head.", player_name, "you are standing in front of them. Your choice… this could be the end it could not be…what do you do?")
        print()
        print("1. Pass through gate")
        print("2. Stay standing in front of the gate")
        print()
    
    
        while True:
            choice = input("What is your choice? ")
            print()
    
            if choice == "1":
                enter_image = graphics.Image(graphics.Point(display_module.WIDTH/2, display_module.HEIGHT/2), "gate_1.png")
                enter_image.draw(win)
                print("-" * 30)
                print("What a terrible mistake", player_name, "you should’ve listened to your upperclassmen! Never pass through the gates before Commencement Day. Oh no you won’t graduate now…")
                return -70
    
            elif choice == "2":
                stand_image = graphics.Image(graphics.Point(display_module.WIDTH/2, display_module.HEIGHT/2), "gate_2.png")
                stand_image.draw(win)
                print("-" * 30)
                print("Excellent choice", player_name, "you listened to your upperclassmen well! You keep your good luck in graduating.")
                return +70
    
            else:
                print("Error you must choose 1 or 2")
                continue
    
        return gate

