'''
In this file, three types of motions are defined: wave one hand, reach hand and don't know gesture

'''
import naoqi
import nao_nocv_2_1 as nao
from naoqi import *


### Connect the robot
robot_IP = "192.168.0.102"
nao.InitProxy(robot_IP)

# Choregraphe motion
def waveOneHand():
    names = list()
    times = list()
    keys = list()

    names.append("HeadPitch")
    times.append([0])
    keys.append([[-0.17, [3, -0.0333333, 0], [3, 0, 0]]])

    names.append("HeadYaw")
    times.append([0])
    keys.append([[0, [3, -0.0333333, 0], [3, 0, 0]]])

    names.append("LAnklePitch")
    times.append([0])
    keys.append([[0.0874194, [3, -0.0333333, 0], [3, 0, 0]]])

    names.append("LAnkleRoll")
    times.append([0])
    keys.append([[-0.110793, [3, -0.0333333, 0], [3, 0, 0]]])

    names.append("LElbowRoll")
    times.append([0])
    keys.append([[-0.417324, [3, -0.0333333, 0], [3, 0, 0]]])

    names.append("LElbowYaw")
    times.append([0])
    keys.append([[-1.20229, [3, -0.0333333, 0], [3, 0, 0]]])

    names.append("LHand")
    times.append([0])
    keys.append([[0.3, [3, -0.0333333, 0], [3, 0, 0]]])

    names.append("LHipPitch")
    times.append([0])
    keys.append([[0.127419, [3, -0.0333333, 0], [3, 0, 0]]])

    names.append("LHipRoll")
    times.append([0])
    keys.append([[0.119108, [3, -0.0333333, 0], [3, 0, 0]]])

    names.append("LHipYawPitch")
    times.append([0])
    keys.append([[-0.17001, [3, -0.0333333, 0], [3, 0, 0]]])

    names.append("LKneePitch")
    times.append([0])
    keys.append([[-0.0923279, [3, -0.0333333, 0], [3, 0, 0]]])

    names.append("LShoulderPitch")
    times.append([0])
    keys.append([[1.44248, [3, -0.0333333, 0], [3, 0, 0]]])

    names.append("LShoulderRoll")
    times.append([0])
    keys.append([[0.224374, [3, -0.0333333, 0], [3, 0, 0]]])

    names.append("LWristYaw")
    times.append([0])
    keys.append([[0.1, [3, -0.0333333, 0], [3, 0, 0]]])

    names.append("RAnklePitch")
    times.append([0])
    keys.append([[0.0874194, [3, -0.0333333, 0], [3, 0, 0]]])

    names.append("RAnkleRoll")
    times.append([0])
    keys.append([[0.110789, [3, -0.0333333, 0], [3, 0, 0]]])

    names.append("RElbowRoll")
    times.append([0, 2.5, 3.9])
    keys.append([[0.417324, [3, -0.0333333, 0], [3, 0.833333, 0]], [0.417324, [3, -0.833333, 0], [3, 0.466667, 0]],
                 [0.417324, [3, -0.466667, 0], [3, 0, 0]]])

    names.append("RElbowYaw")
    times.append([0, 2.5, 3.9])
    keys.append([[1.20229, [3, -0.0333333, 0], [3, 0.833333, 0]], [1.24862, [3, -0.833333, 0], [3, 0.466667, 0]],
                 [1.24862, [3, -0.466667, 0], [3, 0, 0]]])

    names.append("RHand")
    times.append([0])
    keys.append([[0.3, [3, -0.0333333, 0], [3, 0, 0]]])

    names.append("RHipPitch")
    times.append([0])
    keys.append([[0.127419, [3, -0.0333333, 0], [3, 0, 0]]])

    names.append("RHipRoll")
    times.append([0])
    keys.append([[-0.119102, [3, -0.0333333, 0], [3, 0, 0]]])

    names.append("RHipYawPitch")
    times.append([0])
    keys.append([[-0.17001, [3, -0.0333333, 0], [3, 0, 0]]])

    names.append("RKneePitch")
    times.append([0])
    keys.append([[-0.0923279, [3, -0.0333333, 0], [3, 0, 0]]])

    names.append("RShoulderPitch")
    times.append([0, 2.5, 3.9])
    keys.append([[1.69069, [3, -0.0333333, 0], [3, 0.833333, 0]], [-0.581069, [3, -0.833333, 0], [3, 0.466667, 0]],
                 [-0.581069, [3, -0.466667, 0], [3, 0, 0]]])

    names.append("RShoulderRoll")
    times.append([0, 1.7, 2.5, 3.3, 3.9, 4.2])
    keys.append([[-0.277507, [3, -0.0333333, 0], [3, 0.566667, 0]],
                 [-0.265456, [3, -0.566667, -0.0120515], [3, 0.266667, 0.00567129]],
                 [0.104155, [3, -0.266667, 0], [3, 0.266667, 0]],
                 [-0.265456, [3, -0.266667, 0.0985075], [3, 0.2, -0.0738806]], [-0.413009, [3, -0.2, 0], [3, 0.1, 0]],
                 [-0.265456, [3, -0.1, 0], [3, 0, 0]]])

    names.append("RWristYaw")
    times.append([0])
    keys.append([[0.0925025, [3, -0.0333333, 0], [3, 0, 0]]])

    try:
        motion = ALProxy("ALMotion", robot_IP, 9559)
        motion.angleInterpolationBezier(names, times, keys)
    except BaseException, err:
        print err

# Self-defined motion
def reachHand():
    # Choregraphe bezier export in Python.
    from naoqi import ALProxy
    names = list()
    times = list()
    keys = list()

    names.append("RElbowRoll")
    times.append([0.96])
    keys.append([[1.31284, [3, -0.333333, 0], [3, 0, 0]]])

    names.append("RElbowYaw")
    times.append([0.96])
    keys.append([[0.709012, [3, -0.333333, 0], [3, 0, 0]]])

    try:
        motion = ALProxy("ALMotion", robot_IP, 9559)
        motion.angleInterpolationBezier(names, times, keys);
    except BaseException, err:
        print err

# Import from Rctue
def dontKnow():
    # Choregraphe bezier export in Python.
    from naoqi import ALProxy
    names = list()
    times = list()
    keys = list()

    names.append("LShoulderPitch")
    times.append([0.50000, 1.00000])
    keys.append([[1.62490, [3, -0.16667, 0.00000], [3, 0.16667, 0.00000]],
                 [1.39626, [3, -0.16667, 0.00000], [3, 0.00000, 0.00000]]])

    names.append("LShoulderRoll")
    times.append([0.50000, 1.00000])
    keys.append([[0.00873, [3, -0.16667, 0.00000], [3, 0.16667, 0.00000]],
                 [0.34907, [3, -0.16667, 0.00000], [3, 0.00000, 0.00000]]])

    names.append("LElbowYaw")
    times.append([0.50000, 1.00000])
    keys.append([[-2.08567, [3, -0.16667, 0.00000], [3, 0.16667, 0.00000]],
                 [-1.39626, [3, -0.16667, 0.00000], [3, 0.00000, 0.00000]]])

    names.append("LElbowRoll")
    times.append([0.50000, 1.00000])
    keys.append([[-0.88488, [3, -0.16667, 0.00000], [3, 0.16667, 0.00000]],
                 [-1.04720, [3, -0.16667, 0.00000], [3, 0.00000, 0.00000]]])

    names.append("LWristYaw")
    times.append([0.50000, 1.00000])
    keys.append([[-1.82387, [3, -0.16667, 0.00000], [3, 0.16667, 0.00000]],
                 [-0.00000, [3, -0.16667, 0.00000], [3, 0.00000, 0.00000]]])

    names.append("LHand")
    times.append([0.50000, 1.00000])
    keys.append([[0.01745, [3, -0.16667, 0.00000], [3, 0.16667, 0.00000]],
                 [0.00000, [3, -0.16667, 0.00000], [3, 0.00000, 0.00000]]])

    names.append("RShoulderPitch")
    times.append([0.50000, 1.00000])
    keys.append([[1.62490, [3, -0.16667, 0.00000], [3, 0.16667, 0.00000]],
                 [1.39626, [3, -0.16667, 0.00000], [3, 0.00000, 0.00000]]])

    names.append("RShoulderRoll")
    times.append([0.50000, 1.00000])
    keys.append([[-0.00873, [3, -0.16667, 0.00000], [3, 0.16667, 0.00000]],
                 [-0.34907, [3, -0.16667, 0.00000], [3, 0.00000, 0.00000]]])

    names.append("RElbowYaw")
    times.append([0.50000, 1.00000])
    keys.append([[2.08567, [3, -0.16667, 0.00000], [3, 0.16667, 0.00000]],
                 [1.39626, [3, -0.16667, 0.00000], [3, 0.00000, 0.00000]]])

    names.append("RElbowRoll")
    times.append([0.50000, 1.00000])
    keys.append([[0.88488, [3, -0.16667, 0.00000], [3, 0.16667, 0.00000]],
                 [1.04720, [3, -0.16667, 0.00000], [3, 0.00000, 0.00000]]])

    names.append("RWristYaw")
    times.append([0.50000, 1.00000])
    keys.append([[1.82387, [3, -0.16667, 0.00000], [3, 0.16667, 0.00000]],
                 [0.00000, [3, -0.16667, 0.00000], [3, 0.00000, 0.00000]]])

    names.append("RHand")
    times.append([0.50000, 1.00000])
    keys.append([[0.01745, [3, -0.16667, 0.00000], [3, 0.16667, 0.00000]],
                 [0.00000, [3, -0.16667, 0.00000], [3, 0.00000, 0.00000]]])

    try:
        motion = ALProxy("ALMotion", robot_IP, 9559)
        motion.angleInterpolationBezier(names, times, keys);
    except BaseException, err:
        print err
