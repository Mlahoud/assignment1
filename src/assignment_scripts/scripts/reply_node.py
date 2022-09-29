#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist

class reply():
    x_vel = 0.0
    y_vel = 0.0
    ang_vel = 0.0

    def odometry_callback(self, data):
        self.pub.publish(data.twist.twist)
        
    def start_node(self):
        rospy.init_node('reply_node', anonymous=True)
        rospy.Subscriber("/odom", Odometry, self.odometry_callback)
        self.pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=1)
        rospy.spin()

if __name__ == '__main__':
    node = reply()
    node.start_node()