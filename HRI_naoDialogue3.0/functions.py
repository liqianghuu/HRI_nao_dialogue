'''
This file stores all functions related to the main_dialog.py script
'''

import naoqi
import nao_nocv_2_1 as nao
import time
import numpy as np
from naoqi import *
import scenario as scn
from wordslist import Wordlist
import motion

### Import wordlist class
wordlist = Wordlist()

### Connect the robot
robot_IP = "192.168.0.102"
nao.InitProxy(robot_IP)
asr = ALProxy("ALSpeechRecognition", robot_IP, 9559)

### Robot offer the menu
def offerwhat():
    nao.Say("yes, we have beef tartare and Italian meatballs. But we also have food like salad with "
            "mozzarella or with black beans and Savory Oatmeal with Avocado and Poached Egg, if you'd like.")
    nao.Say("what you'd like have?")
    nao.EyeLED([60, 60, 60])
    order_dish = scn.getanswer(wordlist.dish_list + wordlist.repeat_list)
    print (order_dish)
    return order_dish

### Customer initiate order process. Add the dish / alcohol / otherdrinks into the order
def ordersth(order_dish, order_history):
    if len(order_dish) > 0:
        if order_dish[0] in wordlist.dish_list:
            nao.Say("Sure, one of the" + order_dish[0])
            order_history.append(order_dish[0])
            print (order_history)
            order_dish, order_history = ordersthelse(order_dish, order_history)

        if order_dish[0] in wordlist.otherdrinks_list:
            nao.Say("Sure, one of the" + order_dish[0])
            order_history.append(order_dish[0])
            print (order_history)
            order_dish, order_history = ordersthelse(order_dish, order_history)

        elif order_dish[0] in wordlist.alcohol_list:
            nao.Say("Yes, we do provide that. Are you over 18 years old?")
            adult = scn.getanswer(wordlist.yes_list + wordlist.no_list)

            if adult[0] in wordlist.yes_list:
                nao.Say("That would be great. I just have to confirm that.")
                nao.Say("One of the" + order_dish[0])
                order_history.append(order_dish[0])
                print (order_history)
                order_dish, order_history = ordersthelse(order_dish, order_history)

            elif adult[0] in wordlist.no_list:
                nao.Say("Sorry. It is not allowed to take alcohol if you are under 18. "
                        "We do have many non-alcoholic drink. Like soda, juice, tea, coffee Americano.")
        else:
            nao.Say("Sorry, we don't provide that. ")
            motion.dontKnow()

    return order_dish, order_history

### Customer want to order something else. Initate order process
def ordersthelse(order_dish, order_history):
    while order_dish[0] in wordlist.dish_list:
        nao.Say("Do you want to order something else?")
        nao.EyeLED([60, 60, 60])
        yon = scn.getanswer(wordlist.yes_list + wordlist.no_list)

        if yon[0] in wordlist.yes_list:
            nao.Say("Cool! What you'd like to have?")
            nao.Say("You are always welcome to ask me about avaliable options")
            order_dish = scn.getanswer(wordlist.dish_list + wordlist.repeat_list)
            if len(order_dish) > 0:
                if order_dish[0] in wordlist.dish_list:
                    nao.Say("Sure, one of the" + order_dish[0])
                    order_history.append(order_dish[0])
                    print (order_history)
        elif yon[0] in wordlist.no_list:
            nao.say("Okay then!")
            return order_dish, order_history

    return order_dish, order_history
