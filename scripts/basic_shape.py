#!/usr/bin/env python

"""The purpouse of the script is to get de RGB values from /color topic, 
beeing published by rosserial, and try to visualize them in a way in rviz


I found that markers use in their definition a ColorRGBA message and thought I could work with that, 
becuase right now I can't find another way to display RGB data in rviz.
"""

import rospy
import random
from visualization_msgs.msg import Marker
from std_msgs.msg import ColorRGBA

#global Marker type object, atm don't know how to implement in other way
marker = Marker()

def callback(data, marker):

    marker.color.r = data.r/100
    marker.color.g = data.g/100
    marker.color.b = data.b/100
    #marker.color.a = random.randint(1,10)
    marker.color.a = 1

def basic_shape():

    #rospy.init_node('get_color', anonymous=True)
    marker_pub = rospy.Publisher('visualization_marker', Marker, queue_size=10)
    rospy.init_node('basic_shapes', anonymous=True)
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        
        
        marker.header.frame_id = "/my_frame"
        marker.header.stamp = rospy.Time.now()
        marker.ns = "basic_shapes"
        marker.id = 0
        marker.type = 1 # this is a cube

        marker.pose.position.x = 0
        marker.pose.position.y = 0
        marker.pose.position.z = 0
        marker.pose.orientation.x = 0.0
        marker.pose.orientation.y = 0.0
        marker.pose.orientation.z = 0.0
        marker.pose.orientation.w = 1.0

        marker.scale.x = 1.0
        marker.scale.y = 1.0
        marker.scale.z = 1.0
     
        rospy.Subscriber("color", ColorRGBA, callback, marker)
        #print(marker)
        marker.lifetime = rospy.Duration()
        marker_pub.publish(marker)
        rate.sleep()

if __name__ == '__main__':
    try:
        basic_shape()
    except rospy.ROSInterruptException:
        pass
