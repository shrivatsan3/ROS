#!/usr/bin/env python
"""
Created on Wed Jan 12 13:55:16 2022

@author: shriv
"""
#this code probably wont work. Its purpose is to demonstrate
# and give an idea on how a ROS service is written and executed.
#create your own my_package and workspace to make it work.


from my_package.srv import *
import rospy

def service_handle(req):
    
    return AddTwoIntsResponse(req.a+req.b)
    # I know the definition of the service class
    # Therefore I know the fields a and b of the service class
    
    # AddTwoIntsResponse service class will allocate the result of
    # req.a+req.b to the sum field.
    
    # remember on running catkin_make, three service classes are created,
    #AddTwoInts
    #AddTwoIntsRequest
    #AddTwoIntsResponse
    

def add_two_ints_server():
    rospy.init_node('add_two_ints_server') #initialize the ROS node
    
    s = rospy.Service('add_two_ints',AddTwoInts, service_handle)
    # telling the master that I want to offer a service called 
    # 'add_two_ints' which will use the service class AddTwoInts
    
    # I know where this class is since I'm importing all the srv files
    # from my_package
    
    # when we recieve a request, the callback handle takes care of it
    
    rospy.spin() # keeps the node alive 
    
    
