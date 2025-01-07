'''
2023/06/26 17:08
This is the main file of the document, where the overall dialogue, navigation, and gestures will be used.
'''
import naoqi
import nao_nocv_2_1 as nao
import time
import numpy as np
from naoqi import *
import scenario as scn
from wordslist import Wordlist
import functions
import motion1
import navigation as nvg

### Connect the robot
robot_IP = "192.168.0.102"   #varied based on Nao
asr = ALProxy("ALSpeechRecognition", robot_IP, 9559)
at = ALProxy("ALTouch", robot_IP, 9559)

### Import wordlist class
wordlist = Wordlist()

###scenario.py has four functions
"""
twoway(wordList1,wordList2,spk) is used when there're two answers, spk sould be a form of ["Nao says for answer1". "Nao says for answer1"]
sameanswer(wordList,spk) is used whenever we want the human start a dialog. wordList is the dected word, and spk is what Nao responds ["nao says"]
getanswer(wordList) is used to recognized the anser. wordList can be every thing, eg. yes_words + no_words + ["tired","sleepy"]
count_orders(lst) is used to sumarize the order history and combine it in the form of ["you have ordered ", "number1 + dish_name", "number2 + dish_name2"....]
"""


### Part 1  --  Greeting: Welcome the customer
def greetings():
    motion1.waveOneHand()
    nao.Say("Hi! Welcome to the Hub restaurant! Have you reserve the table yet?")
    nao.EyeLED([60, 60, 60])
    result1 = scn.twoway(wordlist.yes_list, wordlist.no_list, ["great can I have your name please?",
                                                                   "Okay, can you tell me how many people will be dining today?"])
    nao.EyeLED([60, 60, 60])
    result2 = ["no"]
    if result1[0] in wordlist.yes_list:
        name = scn.sameanswer(["Amy", "Tom"], ["Okay, I have found your reservation!"])
        nao.Say("welcome!" + name[0] + "! follow me please!")

    elif result1[0] in wordlist.no_list:
        while result2[0] in wordlist.no_list:
            number = scn.sameanswer(["one", "two", "three", "four", "five", "six"], ["table for"])
            nao.Say(number[0] + "right?")
            time.sleep(0.5)
            result2 = scn.twoway(wordlist.yes_list, wordlist.no_list,
                                ["cool, follow me please", "My apologize, can you tell me the numbers again?"])

### Part 2  --  Ordering: Offer customer about the order, give recommendations
def order():
    order_history = []
    order_dish = []
    list = ["have", "menu", "order"]
    time.sleep(0.5)
    nao.Say("Alright so here's your table and the menu, please let me know whenever you're ready for ordering!")
    motion1.reachHand()
    ordering = scn.getanswer(list + wordlist.recommend_list)
    #when asking for what's on the manu
    if ordering[0] in list:
        time.sleep(0.2)
        order_dish = ["have"]  # set order_dish as ["have"] to get in the while loop
        while order_dish[0] in wordlist.repeat_list:  # use while loop to make it repeatable
            order_dish = functions.offerwhat()  # Nao says what the restaurant offers
            order_dish, order_history = functions.ordersth(order_dish, order_history)  # ask if the custemer needs anything else

    elif ordering[0] in wordlist.recommend_list:
        time.sleep(0.2)
        rec_dish = wordlist.get_random_dish()  # select a dish randomly as recommendation
        print rec_dish  # print the dish
        nao.Say("To be honest, as a robot I have no taste but I do know that the." + rec_dish + ".is a huge hit and people love it. Would you like to order one?")
        rec = scn.getanswer(wordlist.yes_list + wordlist.no_list)  # recognize voice
        order_dish = [rec_dish]
        print order_dish

        if rec[0] in wordlist.yes_list:  # if the customers wants it
            nao.Say("Nice choice! Your order has been reserved!")
            order_history.append(order_dish[0])  # add the dish into order history
            print (order_history)
            time.sleep(0.2)

        elif rec[0] in wordlist.no_list:  # if the customer does not want it
            nao.Say("Okay then.")  # do nothing

        order_dish, order_history = functions.ordersthelse(order_dish, order_history)  # ask if they want anything else

        while order_dish[0] in wordlist.repeat_list:  # when they ask for avaliability
            order_dish = functions.offerwhat()  # Nao says what the restaurant offers
            order_dish, order_history = functions.ordersth(order_dish, order_history)  # ask if the custemer need anything else

        print (order_history)  # print the total order history
        if len(order_history) > 0:
            final_order = scn.count_orders(order_history)
            nao.Say(final_order)  # nao say what have been ordered
            nao.Say("Your order has been reserved. Thank you very much for your order.")

### Part 3  --  Check-Out
def checkout():
    Proposal1 = ["Do you want to pack the rest of the food? "]
    Proposal2 = ["How would you like to pay the bill? By card or in cash? "]
    Proposal3 = ["Your bill will be 23.4 euros you can just put your money here in my"]

    scn.sameanswer(wordlist.done_list, Proposal1)  # when the customer said words about check out
    packup = scn.getanswer(wordlist.yes_list + wordlist.no_list)  # ask if they want to pack the rest of food

    if packup[0] in wordlist.yes_list:  # if yes
        nao.Say("I will pack it for you right away." + Proposal2[0])
    elif packup[0] in wordlist.no_list:  # if no
        nao.Say("Sure. Hope you enjoyed your meal!" + Proposal2[0])

    payway = scn.getanswer(wordlist.payment_list)  # ask how they'd like to pay card/cash?

    if payway[0] == "cash":
        nao.Say(Proposal3[0] + ".pocket! Please notice that I only accept the paper money, thanks!")

    elif payway[0] == "card":
        nao.Say(Proposal3[0] + ".hand! Please notice that I only accept Mastro and Visa!")



### Scenario 1 -- Thank you / Ask for help
def scenario_detection():
    scn.twoway(wordlist.thankyou_list, wordlist.greetings_list,
            ["Anything for you! I strive to provide the best assistance possible. Your kind words mean a lot to me.",
                    "hi,how can I help you?"])

### Scenario 2 -- Toilet
def guide_toilet():
    scn.sameanswer(wordlist.wc_list, ["Hi! You are looking for toilet? It is at the end of the main corridor.Do you need me to guide you there?"])
    guid = scn.getanswer(wordlist.yes_list + wordlist.no_list) #detect if the customer need to be guided there
    if guid in wordlist.yes_list:
        nao.Say("cool! please follow me!")
        nvg.search_landmark() #360 degree search for landmark, once searched move towards the target until it's near enough
        nao.Say("there we are!") #once arrives
    elif guid in wordlist.no_list:
        nao.Say("Anything for you.")

### Scenario 3 -- Goodbye
def goodbye():
    scn.sameanswer(wordlist.bye_list, ["Bye-bye! Thank you very much! Have a nice day!"])
    motion1.waveOneHand()
    
### Scenario 4 -- Self-introduction
def introduction():
    scn.sameanswer(wordlist.howareyou_list, ["I'm doing great, thank you for asking. how about you?"])
    hay = scn.getanswer(wordlist.happy_list + wordlist.unhappy_list + wordlist.hungry_list + wordlist.thirsty_list)
    if hay in wordlist.happy_list:
        nao.Say("It's good to know that. I am happy as well, although you might not be able to tell that.")
    elif hay in wordlist.unhappy_list:
        nao.Say("Oh what happened?")
        nao.EyeLED([60,60,60])
    elif hay in wordlist.hungry_list:
        nao.Say("You could order some food if you'd like. I mean, I am your chef and your waitor anyway.")
    elif hay in wordlist.thirsty_list:
        nao.Say("Do you want some drinks? We provide beer, Mojito cocktail and fruit Martini for alcoholic drink. And we also have non-alcoholic opitions.")
        nao.EyeLED([60, 60, 60])
