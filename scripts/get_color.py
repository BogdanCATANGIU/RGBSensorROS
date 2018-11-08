#!/usr/bin/env python

"""Node that subscribes to /color topic and prints out the data.
Same functionality as "rostopic echo /color"
"""

import rospy
from std_msgs.msg import ColorRGBA


def callback(data):
    
    print(data)
    
def get_color():

    rospy.init_node('get_color', anonymous=True)
    rospy.Subscriber("color", ColorRGBA, callback)
    rospy.spin()

if __name__ == '__main__':
    get_color()
