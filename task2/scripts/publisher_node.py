#!/usr/bin/env python

import rospy
from std_msgs.msg import String

if __name__=='__main__':
    pub = rospy.Publisher('team_abhiyaan',String,queue_size=10)
    rospy.init_node('publisher_node',anonymous=True)
    req_str = "Team Abhiyaan Rocks"
    rospy.sleep(0.1)
    rospy.loginfo(req_str)
    pub.publish(req_str)
    rospy.sleep(0.1)
    while not rospy.is_shutdown():
        pass
