#!/usr/bin/env python
"""
Created on Wed Jan 12 11:47:10 2022

@author: shriv
"""


import rospy 
from std_msg.msgs import Strings #rospy takes msg file specified in the 
                                 # CMakeLists.txt file and generates python
                                 # source code for them

def callback(data):
    rospy.loginfo("I heard %s",data.data)
    # displays message on the terminal

def listener():
    rospy.init_node('node_name') #initialize the node
    
    rospy.Subscriber('chatter',String,callback)
    # this subscriber is subscribing to a topic called chatter.
    # whenver we get a message on chatter, we invoke the callback function
    # and it will read the message on chatter
    
    rospy.spin()
    # the subscirber is event driven. its waiting and listening on messages
    # ros.spin keeps the node alive 
