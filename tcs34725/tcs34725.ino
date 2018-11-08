#include <Wire.h>
#include "Adafruit_TCS34725.h"
#include <ros.h>
#include <std_msgs/ColorRGBA.h>

/* Code for the Adafruit TCS34725 RGB sensor to publish messages in ROS using ros_serial*/

/* Connect SCL    to analog 5
   Connect SDA    to analog 4
   Connect VDD    to 3.3V DC
   Connect GROUND to common ground */
   
/* Initialise with default values (int time = 2.4ms, gain = 1x) */
 //Adafruit_TCS34725 tcs = Adafruit_TCS34725();

/* Initialise with specific int time and gain values */
Adafruit_TCS34725 tcs = Adafruit_TCS34725(TCS34725_INTEGRATIONTIME_700MS, TCS34725_GAIN_1X);


/* Setup the node and the publisher */

std_msgs::ColorRGBA color_temp;
ros::Publisher pub_color("color", &color_temp);
ros::NodeHandle nh;


void setup(void) {
  Serial.begin(9600);
  nh.initNode();
  nh.advertise(pub_color);
  
  // Now we're ready to get readings!
}

void loop(void) {
  uint16_t r, g, b, c, colorTemp, lux;
  
  tcs.getRawData(&r, &g, &b, &c);
  //colorTemp = tcs.calculateColorTemperature(r, g, b);
  //lux = tcs.calculateLux(r, g, b);

  color_temp.r=(float)r;
  color_temp.g=(float)g;
  color_temp.b=(float)b;
  color_temp.a=0.0;

  pub_color.publish(&color_temp);
  nh.spinOnce();
}
