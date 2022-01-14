#!/usr/bin/env python
"""
Created on Fri Jan 14 12:07:33 2022

@author: shriv
"""

#The client does not have to be a ROS node
# meaning it doesn't have to be a an executable with a specific functionality
# registered with the ROS master.
# It won't show up in the RQT graph and is not a TCP node

import sys
import rospy
from my_package.srv import *

def add_two_clients(x, y):
    rospy.wait_for_service('add_two_ints')
    # Checking if this service is available
    add_two_ints = rospy.ServiceProxy('add_two_ints', AddTwoInts)
    # 'add_two_ints' is the name of the service to be made 
    # and AddTwoInts is the name of the service class
    # add_two_ints is the handle I will use for the service
    
    response = add_two_ints(x,y)
    return response.sum
    # I know that response has a field called sum from the service 
    # class definition
    