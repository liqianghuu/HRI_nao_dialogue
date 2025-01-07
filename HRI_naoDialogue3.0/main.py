'''
This is the main file of the document, where the overall dialogue, navigation, and gestures will be used.
'''
import naoqi
import nao_nocv_2_1 as nao
from naoqi import *
from wordslist import Wordlist
import main_dialog

### Connect the robot
robot_IP = "192.168.0.102"
nao.InitProxy(robot_IP)
asr = ALProxy("ALSpeechRecognition", robot_IP, 9559)

### Import wordlist class
wordlist = Wordlist()

def main():
    main_dialog.greetings()
    main_dialog.order()
    main_dialog.checkout()

    #Other scenarios
    main_dialog.introduction()
    main_dialog.guide_toilet()

if __name__=="__main__":
    main()