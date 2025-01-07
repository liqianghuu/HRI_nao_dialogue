# Naoqi-Restaurant Assisstant

This is a university Project for interacting with NAO socially with python 2.7 library with naoqi.

## setting up everything thats needed

- adjust the connection settings (ROBOT_IP & ROBOT_PORT). 
- start the script

## file explanation
- **main.py** initiates the program.
- **main_dialog.py** the main dialogue file of the document, where the overall dialogue, navigation, and gestures will be used.
- **functions.py** stores all functions related to the main_dialog.py script 
- **scenario.py** defines some basic and reusable functions in the dialogue.
- **navigation.py** sets landmark detection and moves towards the landmark function
- **wordslist.py** provides the overall wordlist that robot might recognize or respond to the customer.
- **motion1.py** contains the state machine diagram of the whole process
- **nao_nocv_2_1.py** contains all configuration functions to interact with the robot.
- **state_machine_a3.py** shows the state machine diagram of the process

## Scenario
This scenario is based on the assignment 2, where a robot serves as a waitor in the restaurant.
