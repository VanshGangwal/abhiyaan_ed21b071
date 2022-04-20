#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def sub_ka_kaam(data):
    rospy.sleep(0.1)
    rospy.loginfo("From subscriber node ...\n%s",data.data)

if __name__=='__main__':
    rospy.sleep(0.1)
    rospy.init_node('subscriber_node',anonymous=True)
    rospy.sleep(0.1)
    rospy.loginfo("Subscriber node has started...")
    rospy.sleep(0.1)
    sub = rospy.Subscriber("team_abhiyaan",String,callback=sub_ka_kaam)
    
    rospy.spin()