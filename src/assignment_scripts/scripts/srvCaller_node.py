#!/usr/bin/env python

from __future__ import print_function
from operator import gt

import sys
import rospy
from assignment_scripts.srv import randPos
from robot_description.srv import Position
from std_msgs.msg import String

def randPos_client(min, max):
    rospy.wait_for_service('random-position')
    try:
        randPos_srv = rospy.ServiceProxy('random-position', randPos)
        resp1 = randPos_srv(min, max)
        return resp1
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

def gtp_client(x, y, theta):
    rospy.wait_for_service('/go_to_point')
    try:
        gtp_srv = rospy.ServiceProxy('/go_to_point', Position)
        resp2 = gtp_srv(x, y, theta)
        return resp2
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

def srvCaller():
    
    rospy.init_node('srv_caller', anonymous=True)
    rate = rospy.Rate(1) # 10hz
    while not rospy.is_shutdown():
        rospy.loginfo("Getting position")
        rp = randPos_client(1.0, 9.0)
        print("go to random position = %s"%rp)
        gtp_client(rp.x, rp.y, rp.theta)
        rate.sleep()

if __name__ == '__main__':
    try:
        srvCaller()
    except rospy.ROSInterruptException:
        pass