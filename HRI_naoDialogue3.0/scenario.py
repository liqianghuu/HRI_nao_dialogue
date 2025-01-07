'''
This file defines some basic and reusable functions in the dialogue.
'''
import naoqi
import nao_nocv_2_1 as nao
import time
import numpy as np
from naoqi import *
from collections import Counter
from wordslist import Wordlist

wordlist = Wordlist()

"""
twoway(wordList1,wordList2,spk) is used when there're two answers, spk sould be a form of ["Nao says for answer1". "Nao says for answer1]
eg. twoway (["yes"],["no","nah"],["great!","okay then"])
when the person says the word"yes", nao will say "great!"
when the person says the word "no" or "nah", nao will say "okay then"
"""
def twoway(wordList1,wordList2,spk):
    maxcount = 50
    the_language = "English"
    nao.InitSpeech(wordList1 + wordList2, the_language)
    count = 0
    nao.asr.subscribe("MyModule")
    while count < maxcount:
        result = nao.DetectSpeech()
        if len(result) > 0:
            if result[0] in wordList1:
                print result
                nao.asr.unsubscribe("MyModule")
                nao.Say(spk[0])
                time.sleep(0.2)
                nao.asr.subscribe("MyModule")
                count = 99
            elif result[0] in wordList2:
                print result
                nao.asr.unsubscribe("MyModule")
                nao.Say(spk[1])
                time.sleep(0.2)
                nao.asr.subscribe("MyModule")
                count = 99
        else:
            nao.Say("I am sorry, I don't understand you. Can you repeat that again?")
            print "Word not in the wordlist error"

        time.sleep(0.5)
        count = count + 1

    nao.asr.unsubscribe("MyModule")
    return result


"""
sameanswer(wordList,spk) is used whenever we want the human start a dialog. wordList is the dected word, and spk is what Nao responds ["nao says"]
eg. sameanswer(["hello","hey","hi","how are you"],["hello world"])
when the person says any greeting word, nao will respond "hello world"
"""
def sameanswer(wordList,spk):
    maxcount = 50
    the_language = "English"
    nao.InitSpeech(wordList,the_language)
    count = 0
    nao.asr.subscribe("MyModule")
    while count < maxcount:
        result = nao.DetectSpeech()
        if len(result) > 0:
            print result
            nao.asr.unsubscribe("MyModule")
            nao.Say(spk[0])
            time.sleep(0.2)
            nao.asr.subscribe("MyModule")
            count = 99
        else:
            nao.Say("I am sorry, I don't understand you. Can you repeat that again?")
            print "Word not in the wordlist error"

        time.sleep(0.5)
        count = count + 1

    nao.asr.unsubscribe("MyModule")
    return result


"""
result = getanswer(wordList) is used to recognized the anser. wordList can be every thing,
eg. getanswer(yes_words + no_words + ["tired","sleepy"])
whenever the person say anything within the word lists, it will be saved in result
"""
def getanswer(wordList):
    maxcount = 50
    the_language = "English"
    nao.InitSpeech(wordList,the_language)
    count=0
    nao.asr.subscribe("MyModule")
    while count < maxcount:
        result = nao.DetectSpeech()
        if len(result) > 0:
            print result
            nao.asr.unsubscribe("MyModule")
            time.sleep(0.2)
            nao.asr.subscribe("MyModule")
            count = 99
        else:
            nao.Say("I am sorry, I don't understand you. Can you repeat that again?")
            print "Word not in the wordlist error"

        time.sleep(0.5)
        count = count + 1
    nao.asr.unsubscribe("MyModule")
    return result

"""
count_orders(lst) is used to sumarize the order history and combine it in the form of ["you have ordered ", "number1 + dish_name", "number2 + dish_name2"....]
"""
def count_orders(lst):
    counts = Counter(lst)
    output = ["You have ordered."]
    for string, count in counts.items():
        output.append("{} {}.".format(count, string))
    return " ".join(output)


