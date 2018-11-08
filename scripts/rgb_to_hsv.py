#!/usr/bin/env python

"""
Node that subscribes to /color topic and publishes RGB data in HSV format to /colorHSV.
"""

import rospy
import colorsys
from std_msgs.msg import ColorRGBA
from sensor_fusion.msg import ColorHSV

hsv = ColorHSV()

def callback(data):
    
    temp_hsv = colorsys.rgb_to_hsv(data.r/65535, data.g/65535, data.b/65535)
    hsv.hue = temp_hsv[0]*360 # transform into degrees
    hsv.saturation = temp_hsv[1]
    hsv.value = temp_hsv[2]
    
def convert():

    rospy.init_node('rgb_to_hsv', anonymous=True)
    hsv_pub = rospy.Publisher('colorHSV', ColorHSV, queue_size=10)
    rate = rospy.Rate(10)
    
    while not rospy.is_shutdown():
        rospy.Subscriber("color", ColorRGBA, callback)
        hsv_pub.publish(hsv)
        rate.sleep()   

if __name__ == '__main__':
    try:
        convert()
    except rospy.ROSInterruptException:
        pass
