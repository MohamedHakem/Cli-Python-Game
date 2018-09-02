#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 03:56:00 2018
@author: mohamedhakem
"""

print("""Welcome 
      Now you here so pay attention......
      On front of you there are 3 doors. Which door you will go through out of here :
      door #1 or door #2 or door #3 ?")
      """)      

door = input("> Your Answer: ")

# the door no.1 

if door == "1":
    print("""There's a strange man in a black jacket.
          carrying 2 pills in his hands.
          in the right hand there are a red pill
          and in the left hand a blue pill.
          The man asking you to choose one pill and take it 
          or just go through the door on your left hand.
          The red one will take you home anyway, the blue one will prepare you to the great truth.
          Which pill you will choose.
          Make a choice ( SAW III :') ) ?")
          """)
    print("1. The red pill.")
    print("2. The blue pill.")
    print("3. Going to that door.")
    
    pill = input(">So choose :  ")
    
    if pill == "1":
        print("""So you want the red pill. Fine close your eyes,
              and in 10 seconds you will be at home setting on your computer chatting with me! :' """)
    elif pill == "2":
        print("""So you want the blue pill. That's mean that you want the truth!,
              So take it man and i promise you i will show you the only truth.
              open your hand and i will put the blue pill in it, open it matksfsh :') .""")
    else:
        print("So you choose to go through that door so if sure push 1 or not sure push 2")
        sure = input("> Are you sure or not : ")
        if sure == 1 or sure == 2:
            print("Anyway, 'm sorry the door is locked and i have not the key, so you have to choose one of the pills :' ")
            print("""The red one will take you home, the blue one will show you to the truch,
                  1 for the red or 2 for the blue,
                  Make a choice
                  """)
            red_or_blue = input(">Choose man: ")
            if red_or_blue == "1":
                print("""So you want the red pill. Fine close your eyes,
              and in 10 seconds you will be at home setting on your computer chatting with me! :' """)
            elif red_or_blue == "2":
                print("""So you want the blue pill. That's mean that you want the truth!,
              So take it man and i promise you i will show you the only truth.
              open your hand and i will put the blue pill in it, open it matksfsh :') .""")
            else:
                print("Anyway, sorry but i told you the door is locked and i have not the key, so you have to choose one of the pills :' ")
                print("""The red one will take you home, the blue one will show you to the truth,
                  1 for the red or 2 for the blue,
                  Make a choice
                  """)
                red_or_blue_again = input(">Choose man: ")
                if red_or_blue_again == "1":
                    print("""So you want the red pill. Fine close your eyes,
                  and in 10 seconds you will be at home setting on your computer chatting with me! :' """)
                elif red_or_blue_again == "2":
                    print("""So you want the blue pill. That's mean that you want the truth!,
              So take it man and i promise you i will show you the only truth.
              open your hand and i will put the blue pill in it, open it matksfsh :') .""")
                else:
                    print("Go sleep man and don't play with me again, just go :( ")
              
        else:
            print("Anyway, 'm sorry the door is locked and i have not the key, so you have to choose one of the pills :' ")
            print("""The red one will take you home, the blue one will show you to the truth,
                  1 for the red or 2 for the blue,
                  Make a choice
                  """)
            red_or_blue = input("> Choose man: ")
            if red_or_blue == "1":
                print("""So you want the red pill. Fine close your eyes,
              and in 10 seconds you will be at home setting on your computer chatting with me! :' """)
            elif red_or_blue == "2":
                print("""So you want the blue pill. That's mean that you want the truth!,
              So take it man and i promise you i will show you the only truth.
              open your hand and i will put the blue pill in it, open it matksfsh :') .""")
            else:
                print("Anyway, sorry but i told you the door is locked and i have not the key, so you have to choose one of the pills :' ")
                print("""The red one will take you home, the blue one will show you to the truth,
                  1 for the red or 2 for the blue,
                  Make a choice
                  """)
                red_or_blue_again = input(">Choose man: ")
                if red_or_blue_again == "1":
                    print("""So you want the red pill. Fine close your eyes,
                  and in 10 seconds you will be at home setting on your computer chatting with me! :' """)
                elif red_or_blue_again == "2":
                    print("""So you want the blue pill. That's mean that you want the truth!,
              So take it man and i promise you i will show you the only truth.
              open your hand and i will put the blue pill in it, open it matksfsh :') .""")
                else:
                    print("Go sleep man and don't play with me again, just go :( ")
        
        
        
# the door no.2
            
elif door == "2":
    print("You are in the middle of nowhere what the first thing come to your mind ?")
    print("1. Run heading any direction.")
    print("2. Try using your phone and get signal! .")
    print("3. Just set down and doing nothing.")
    
    decision = input(">: ")
    
    if decision == "1":
        print("""You will find yourself exhausted after a couple of hours,
              and your situation is worse,you are now in the middle of nowhere,
              and also can not move because you tired. Good job!") 
              """)
    elif  decision == "2":
        print("""Fine this is a good thinking so you maybe recieve signal 
              and call someone or even use GBS to know your location.""")
    else:
        print("You just calm so keep calm and you will probably turn into ice. Good job!")

# the door no.3  
        
else:
    print("Oh sorry this just a bathroom. :' :P :P :P ")
    print("\n\n")
    print("""Welcome  again
      So you are here again maybe you missed me :P :P :P ......
      On front of you there are 2 doors now unless you need to use the bathroom :P.
      Which door you will go through :
      door #1 or door #2 ?")
      """)      
    
    door = input("> Your Answer: ")

# door 3 : the door no.1 

    if door == "1":
        print("""There's a strange man in a black jacket.
              carying 2 pills in his hands.
              in the right hand there are a red pill
              and in the left hand a blue pill.
              The man asking you to choose one pill and take it 
              or just go through the door on your left hand.
              The red one will take you home anyway, the blue one will prepare you to the great truch.
              Which pill you will choose.
              Make a choice ( SAW III :') ) ?")
              """)
        print("1. The red pill.")
        print("2. The blue pill.")
        print("3. Going to that door.")
        
        pill = input(">So choose :  ")
        
        if pill == "1":
            print("""So you want the red pill. Fine close your eyes,
                  and in 10 seconds you will be at home setting on your computer chatting with me! :' """)
        elif pill == "2":
            print("""So you want the blue pill. That's mean that you want the truth!,
                  So take it man and i promise you i will show you the only truth.
                  open your hand and i will put the blue pill in it, open it matksfsh :') .""")
        else:
            print("So you choose to go through that door so if sure push 1 or not sure push 2")
            sure = input("> Are you sure or not : ")
            if sure == 1 or sure == 2:
                print("Anyway, 'm sorry the door is locked and i have not the key, so you have to choose one of the pills :' ")
                print("""The red one will take you home, the blue one will show you to the truth,
                      1 for the red or 2 for the blue,
                      Make a choice
                      """)
                red_or_blue = input(">Choose man: ")
                if red_or_blue == "1":
                    print("""So you want the red pill. Fine close your eyes,
                  and in 10 seconds you will be at home setting on your computer chatting with me! :' """)
                elif red_or_blue == "2":
                    print("""So you want the blue pill. That's mean that you want the truth!,
                  So take it man and i promise you i will show you the only truth.
                  open your hand and i will put the blue pill in it, open it matksfsh :') .""")
                else:
                    print("Anyway, sorry but i told you the door is locked and i have not the key, so you have to choose one of the pills :' ")
                    print("""The red one will take you home, the blue one will show you to the truth,
                      1 for the red or 2 for the blue,
                      Make a choice
                      """)
                    red_or_blue_again = input(">Choose man: ")
                    if red_or_blue_again == "1":
                        print("""So you want the red pill. Fine close your eyes,
                      and in 10 seconds you will be at home setting on your computer chatting with me! :' """)
                    elif red_or_blue_again == "2":
                        print("""So you want the blue pill. That's mean that you want the truth!,
                  So take it man and i promise you i will show you the only truth.
                  open your hand and i will put the blue pill in it, open it matksfsh :') .""")
                    else:
                        print("Go sleep man and don't play with me again, just go :( ")
                  
            else:
                print("Anyway, 'm sorry the door is locked and i have not the key, so you have to choose one of the pills :' ")
                print("""The red one will take you home, the blue one will show you to the truth,
                      1 for the red or 2 for the blue,
                      Make a choice
                      """)
                red_or_blue = input(">Choose man: ")
                if red_or_blue == "1":
                    print("""So you want the red pill. Fine close your eyes,
                  and in 10 seconds you will be at home setting on your computer chatting with me! :' """)
                elif red_or_blue == "2":
                    print("""So you want the blue pill. That's mean that you want the truth!,
                  So take it man and i promise you i will show you the only truth.
                  open your hand and i will put the blue pill in it, open it matksfsh :') .""")
                else:
                    print("Anyway, sorry but i told you the door is locked and i have not the key, so you have to choose one of the pills :' ")
                    print("""The red one will take you home, the blue one will show you to the truth,
                      1 for the red or 2 for the blue,
                      Make a choice
                      """)
                    red_or_blue_again = input(">Choose man: ")
                    if red_or_blue_again == "1":
                        print("""So you want the red pill. Fine close your eyes,
                      and in 10 seconds you will be at home setting on your computer chatting with me! :' """)
                    elif red_or_blue_again == "2":
                        print("""So you want the blue pill. That's mean that you want the truth!,
                  So take it man and i promise you i will show you the only truth.
                  open your hand and i will put the blue pill in it, open it matksfsh :') .""")
                    else:
                        print("Go sleep man and don't play with me again, just go :( ")
            
            
            
# door 3 : the door no.2
            
    elif door == "2":
        print("You are in the middle of nowhere what the first thing come to your mind ?")
        print("1. Run heading any direction.")
        print("2. Try using your phone and get signal! .")
        print("3. Just set down and doing nothing.")
        
        insanity = input(">: ")
        
        if insanity == "1":
            print("""You will find yourself exhausted after a couple of hours,
                  and your situation is worse,you are now in the middle of nowhere,
                  and also can not move because you tired. Good job!") 
                  """)
        elif  insanity == "2":
            print("""Fine this is a good thinking so you maybe recieve signal 
                  and call someone or even use GBS to know your location.""")
        else:
            print("You just calm so keep calm and you will probably turn into ice. Good job!")
            
# door 3 : the door no.3
    else:
        print("Go sleep man and don't play with me again, just go :( ")
