# -*- coding: utf-8 -*-
'''
This file sets landmark detection and moves towards the landmark function
First nao will turn its head approximately 120 degrees in front of it to detect the landmark,
if not then turn around 120 degrees and continue to repeat until the 360 enveriment is fully scanned
once locates the landmard, it move towards the landmark till its near enough
'''

import nao_nocv_2_1 as nao
import numpy as np
import time
import math


def search_landmark():
    robot_IP= "192.168.0.112" #might varies
    nao.InitProxy(robot_IP)
    nao.InitPose()
    nao.InitLandMark()

    head_range = np.linspace(-1,1,10)   #head movement range for detection
    body_range = np.linspace(0,6.2832,4)#body movement range for detection (0 120 240)
    detect_times = 100                  #detect 100 times for each angle
    detect_threshhold = 0
     
    for rad1 in body_range:
        nao.Walk(0,0,rad1)              #move body when no landmark detected for that position (0 120 240)
        nao.MoveHead(yaw_val = 0, pitch_val=0, isAbsolute =True)    #move the head to it's original angle
        
        for rad in head_range:
            time.sleep(0.1)             #pause
            nao.MoveHead(yaw_val = rad, pitch_val=0, isAbsolute=True, timeLists=[[1],[1]])  #turn the head and detect landmark
            nao.InitVideo (1)           #open video
            time.sleep (0.1)            #pause 
            for counts in range(detect_times):
                detected, timestamp, markerInfo=nao.DetectLandMark()
                if detected:
                    detect_threshhold += 1
                if (detect_threshhold >=10 ):           #when detected more then 10 times out of 100 times
                    nao.Say ('landmark detected')
                    time.sleep(1)
                    nao.MoveHead(yaw_val = markerInfo[0][1]+rad, pitch_val=0, isAbsolute=True)  #turn the head facing it
                    nao.Walk(0,0,markerInfo[0][1]+rad)                          #turn the body facing it
                    nao.MoveHead(yaw_val = 0, pitch_val=0, isAbsolute =True)    #move the head to it's original angle
                    time.sleep(0.1)
                    break
                    #return detected, markerInfo
            nao.EndVideo()
                
    desired_x = 0.5  # The X position in the desired camera view
    desired_y = 0.3  # The Y position in the desired camera view

    while True:
        detected, timestamp, markerInfo = nao.DetectLandMark() 
        for marker in markerInfo:
            marker_id = marker[0]
            alpha = marker[1]
            beta = marker[2]

            # Calculation of the angle and distance the robot needs to be adjusted
            delta_x = desired_x - alpha
            delta_y = desired_y - beta
            angle = math.atan2(delta_x, delta_y)  # Calculation of the angle to be adjusted
            distance = math.sqrt(delta_x**2 + delta_y**2)  # Calculate the distance to be adjusted
            
            # Adjusting the orientation of the robot
            nao.Walk(0,0,angle)
            nao.MoveHead(yaw_val=0, pitch_val=0, isAbsolute=True, timeLists=[[1], [1]])
                
            # Move robot to target position
            nao.Walk(distance,0,0)
            #Stop
            break
    
        # Check if object tracking and positioning is complete
        if detected and distance < 0.1:
            nao.Say("target assess")
            break
        
        time.sleep(0.1)  # Wait a while and continue the loop
    nao.Crouch()

search_landmark ()
