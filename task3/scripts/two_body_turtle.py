#!/usr/bin/env python3
import rospy
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
from turtlesim.srv import Kill
from turtlesim.srv import Spawn

def turtle_killer(name_of_turtle):
    try:
        killer = rospy.ServiceProxy("/kill",Kill)
        killer(name_of_turtle)
    except rospy.ServiceException as e:
        rospy.logwarn(e)

def spawner(x,y,theta,name_of_turtle):
    try:
        spawnr = rospy.ServiceProxy("/spawn",Spawn)
        spawnr(x,y,theta,name_of_turtle)
    except rospy.ServiceException as e:
        rospy.logwarn(e)

def pose_callback(pose: Pose):
    cmd = Twist()
    cmd.linear.x = 4
    cmd.angular.z = -1
    pub1.publish(cmd)


def pose_callback2(pose: Pose):
    cmd = Twist()
    cmd.linear.x = 2
    cmd.angular.z = -1
    pub2.publish(cmd)

if __name__ == '__main__':
    rospy.init_node("turtle_controller")

    rospy.wait_for_service("/kill")
    turtle_killer("turtle1")

    rospy.wait_for_service("/spawn")
    spawner(1,5.5,1.57,"turtle1")
    spawner(7,5.5,4.71,"turtle2")

    sub1 = rospy.Subscriber("/turtle1/pose",Pose,callback= pose_callback)
    pub1 = rospy.Publisher("/turtle1/cmd_vel",Twist,queue_size=10)

    sub2 = rospy.Subscriber("/turtle2/pose",Pose,callback= pose_callback2)
    pub2 = rospy.Publisher("/turtle2/cmd_vel",Twist,queue_size=10)

    rospy.loginfo("Node has started.")
    rospy.spin()