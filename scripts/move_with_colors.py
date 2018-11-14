#!/usr/bin/env python
'''This node subscribes to /colorHSV topic to get the 
color values and does a defined action for each specific recognised color
by publishing to /cmd_vel topic'''

import rospy
from sensor_fusion.msg import ColorHSV
from geometry_msgs.msg import Twist

color_mapping = { "green" : [ 1, 0 ],   #move forward
                  "orange": [ 1, 1 ],   #move in an arc 
                  "unknown":[ 0, 0 ],   #STOP
                  "blue"  : [-1, 0 ],   #move backwards
                  "pink"  : [ 0, 1 ],   #rotate counter-clockwise
                  "yellow": [ 0, -1]    #rotate clockwise
                 }

g_last_twist = Twist() # initializes to zero
twist_pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)

def determine_color(msg):
    global g_last_twist
    if msg.hue > 81 and msg.hue < 140:
        print("Green detected = FORWARD")
        g_last_twist.linear.x  = color_mapping['green'][0]
        g_last_twist.angular.z = color_mapping['green'][1]
    elif msg.hue > 40 and msg.hue < 60:
        print("Yellow detected = ROTATE CLOCKWISE")
        g_last_twist.linear.x  = color_mapping['yellow'][0]
        g_last_twist.angular.z = color_mapping['yellow'][1]
    elif msg.hue > 331 and msg.hue < 360:
        print("Pink detected = ROTATE COUNTER-CLOCKWISE")
        g_last_twist.linear.x  = color_mapping['pink'][0]
        g_last_twist.angular.z = color_mapping['pink'][1]
    elif msg.hue > 170 and msg.hue < 240:
        print("Blue detected = BACKWARDS")
        g_last_twist.linear.x  = color_mapping['blue'][0]
        g_last_twist.angular.z = color_mapping['blue'][1]
    elif (msg.hue > 0 and msg.hue < 10) or (msg.hue > 357 and msg.hue < 360):
        print("Orange detected = ARC MOVEMENT")
        g_last_twist.linear.x  = color_mapping['orange'][0]
        g_last_twist.angular.z = color_mapping['orange'][1]
    else:
        print("Unknown color detected = STOP MOVEMENT")
        g_last_twist.linear.x  = color_mapping['unknown'][0]
        g_last_twist.angular.z = color_mapping['unknown'][1]
    twist_pub.publish(g_last_twist)

if __name__ == '__main__':
    rospy.init_node('color_move')
    rospy.Subscriber("colorHSV", ColorHSV, determine_color)
    rospy.spin()

    
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        twist_pub.publish(g_last_twist)
        rate.sleep()