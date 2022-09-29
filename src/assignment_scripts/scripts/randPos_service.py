#!/usr/bin/env python

import random
import rospy
from math import pi
from assignment_scripts.srv import randPos

def handle_call(req):
    print("min = %s and max = %s" % (req.min, req.max))
    x = random.uniform(req.min, req.max)
    y = random.uniform(req.min, req.max)
    theta =random.uniform(-pi, pi)
    return [x, y, theta]

def random_position_server():
    rospy.init_node('random-position_server')
    s = rospy.Service('random-position', randPos, handle_call)
    print("Ready to generate random numbers")
    rospy.spin()

if __name__ == "__main__":
    random_position_server()
