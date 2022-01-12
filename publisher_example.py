# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 10:57:36 2022

@author: shriv
"""

import rospy 
from std_msg.msgs import Strings #rospy takes msg file specified in the 
                                 # CMakeLists.txt file and generates python
                                 # source code for them

# creating a handler for publisher object
pub = rospy.Publisher('topic_name', String, queue_size=10)
# if for some reason the messages ar enot being published at a specified rate
# the message is stored onto the buffer so that data is not lost 

# telling ROS this file is an executable
rospy.init_node('node_name')
# also has another argument
#rospy.init_node('node_name', anonymous = True)
# when anonymous is true, ROS appends a psuedo random number to the node
# name as node name has to be uniques

# Specify a rate object, at which messages would be published
r = rospy.Rate(10) # 10 hz

while not rospy.is_shutdown(): # while the value of the shutdown flag is
                               # is not true
                               #Shutdown flag is set when someone presses
                               #exit, or ctrl+c or rosnode kill
                               
    pub.publish("Hello, world!") # publish the message
    
    # or, create a String object
    # msg = String()  
    # msg.data = "Hello, world!" , check msg definiton for fields
    # pub.publish(msg)
    
    r.Sleep() # Smartly figures out how muchto sleep within loop 
              # to maintain publishing rate


