#!/usr/bin/env python
import vrep
import time
import rospy
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(1) # 10hz
    while not rospy.is_shutdown():
        hello_str = "hello world %s" % rospy.get_time()
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()
        returnCode=vrep.simxSetJointTargetVelocity(clientID,leftmotor,31.416,vrep.simx_opmode_streaming)
        returnCode=vrep.simxSetJointTargetVelocity(clientID,rightmotor,31.416,vrep.simx_opmode_streaming)

vrep.simxFinish(-1) # just in case, close all opened connections
clientID=vrep.simxStart('127.0.0.1',19999,True,True,5000,5) # Connect to V-REP
if clientID!=-1:
    print ('Connected to remote API server')
else:
    print('Failed connecting to remote API server')

returnCode = vrep.simxStartSimulation(clientID,vrep.simx_opmode_oneshot)

returnCode,leftmotor = vrep.simxGetObjectHandle(clientID,'DynamicLeftJoint',vrep.simx_opmode_blocking)
returnCode,rightmotor = vrep.simxGetObjectHandle(clientID,'DynamicRightJoint',vrep.simx_opmode_blocking)
returnCode,robot_handle = vrep.simxGetObjectHandle(clientID,'LineTracer',vrep.simx_opmode_blocking)
returnCode,leftsensor = vrep.simxGetObjectHandle(clientID,'LeftSensor',vrep.simx_opmode_blocking)
returnCode,midsensor = vrep.simxGetObjectHandle(clientID,'MiddleSensor',vrep.simx_opmode_blocking)
returnCode,rightsensor = vrep.simxGetObjectHandle(clientID,'RightSensor',vrep.simx_opmode_blocking)

left_sensor1 = 0
mid_sensor1 = 0
right_sensor1 = 0
left_sensor1 = vrep.simxReadVisionSensor(clientID, leftsensor, vrep.simx_opmode_streaming)
mid_sensor1 = vrep.simxReadVisionSensor(clientID, midsensor, vrep.simx_opmode_streaming)
right_sensor1 = vrep.simxReadVisionSensor(clientID, rightsensor, vrep.simx_opmode_streaming)
time.sleep(5)

returnCode=vrep.simxSetJointTargetVelocity(clientID,leftmotor,31.416,vrep.simx_opmode_streaming)
returnCode=vrep.simxSetJointTargetVelocity(clientID,rightmotor,-31.416,vrep.simx_opmode_streaming)

talker()

count=0
time.sleep(5)
'''
while count<50:
    time.sleep(0.1)
    left_sensor1 = vrep.simxReadVisionSensor(clientID, leftsensor, vrep.simx_opmode_streaming)
    mid_sensor1 = vrep.simxReadVisionSensor(clientID, midsensor, vrep.simx_opmode_streaming)
    right_sensor1 = vrep.simxReadVisionSensor(clientID, rightsensor, vrep.simx_opmode_streaming)
    print(left_sensor1[1])
    print(mid_sensor1[1])
    print(right_sensor1[1])
    count = count + 1
#returnCode,position=vrep.simxGetObjectPosition(clientID,robot_handle,-1,vrep.simx_opmode_buffer)
'''
returnCode=vrep.simxSetJointTargetVelocity(clientID,leftmotor,0.31416,vrep.simx_opmode_streaming)
returnCode=vrep.simxSetJointTargetVelocity(clientID,rightmotor,-0.31416,vrep.simx_opmode_streaming)

returnCode = vrep.simxStopSimulation(clientID,vrep.simx_opmode_oneshot)

time.sleep(0.1)
