# RGBSensorROS
Project during Robot Simulation Class to add a RGB sensor in ROS


Implemented a functionality to send std_msgs/cmd_vel based on different colors detected by RGBA sensor.

Worked with Adafruit's TCS34725 RGBA sensor, and implemented a publisher node that sends relevant data through 
ROS ecosystem using Arduino libraries.

Data is transformed in HSV values and based on color detected it sends velocity commands to a turtlebot3, in my case.

Also added some Rviz visualization of the sensed color.

