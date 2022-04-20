#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def whole_reverser(Sentence):
    '''This function will return a string in which the words are reversed but order of the words is same.'''
    words = str.split(Sentence)
    newWords = [word[::-1] for word in words]
    #Now that each word is reversed, we will attach them back together to form a string. 
    newSentence = " ".join(newWords)
    #Returning modified string.
    return newSentence

def recaller(data:String):
    rospy.loginfo("into the function...")
    my_str = data.data
    new_str = whole_reverser(my_str)
    pub.publish(new_str)
    rospy.loginfo(new_str)

if __name__=='__main__':
    rospy.init_node('reverse_sub_node',anonymous=True)
    pub = rospy.Publisher('naayihba_maet',String,queue_size=10)
    sub = rospy.Subscriber('team_abhiyaan',String,recaller)
    
    rospy.spin()    