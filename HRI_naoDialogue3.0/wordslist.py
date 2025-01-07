'''
This file provides the overall wordlist that robot might recognize or respond to the customer.
'''
import random


class Wordlist:
    def __init__(self):
        self.greetings_list = ["hi", "hello", "hey there"]
        self.number_list = ["one", "two", "three", "four", "five"]
        self.yes_list = ["yes", "yep", "sure", "why not", "of course", "certainly", "yeah"]
        self.no_list = ["well", "no", "nah", "not really"]
        self.ok_list = ["cool", "ok", "very well", "got it"]
        self.dont_list = ["don't", "do not", "dont"]
        self.dish_list = ["beef tartare" "salad with Mozzarella" "Italian meatballs" "meatball" "meatballs" "salad" 
                          "Savory Oatmeal with Avocado and Poached Egg" "egg" "beef" "salad with black beans" 
                          "Black bean salad"]
        self.done_list = ["finished", "done", "check out", "bill"]
        self.payment_list = ["cash", "card"]
        self.howareyou_list = ["How was your day?", "How's your day been?", "How about you?", "How's it going today?",
                               "How are you"]
        self.happy_list = ["happy", "nice", "energetic", "tasty", "good", "well", "fine"]
        self.unhappy_list = ["tired", "stressful", "terrible", "disaster", "unhappy", "anxious", "upset", "not good"]
        self.hungry_list = ["hungry", "starving"]
        self.thirsty_list = ["out of water", "thirsty"]
        self.ready_list = ["ready" "long time" "wait"]
        self.repeat_list = ["have", "again", "repeat"]
        self.thankyou_list = ["thank", "appreciate"]

        self.alcohol_list = ["beer", "cocktail", "fruit wine", "fruit martini", "Mojito", "Mojito cocktail"]
        self.otherdrinks_list = ["water", "tap water", "soda", "juice", "tea" "coffee Americano", "coffee"]

        self.toilet_list = ["wc", "toilet", "bathroom"]
        self.have_list = ["have", "provide"]

        self.recommend_list = ["recommendation", "recommend"]
        self.wc_list = ["toilet", "bathroom","wc","pee"]

        self.bye_list = ["goodbye", "bye-bye", "bye"]


    ### Randomize the response
    def get_random_greeting(self):
        return random.choice(self.greetings_list)

    def get_random_number(self):
        return random.choice(self.number_list)

    def get_random_yes(self):
        return random.choice(self.yes_list)

    def get_random_no(self):
        return random.choice(self.no_list)

    def get_random_ok(self):
        return random.choice(self.ok_list)

    def get_random_dont(self):
        return random.choice(self.dont_list)

    def get_random_dish(self):
        return random.choice(self.dish_list)

    def get_random_payment(self):
        return random.choice(self.payment)
