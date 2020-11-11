#!/usr/bin/env python

import rospy
from std_msgs.msg import String
    
def talker1():
    pub = rospy.Publisher('chatter1', String, queue_size=10)
    rospy.init_node('talker1', anonymous=True)
    rate = rospy.Rate( 1 ) # 1hz
    while not rospy.is_shutdown():
        stat = "I'm a software robotics engineer, now learning ROS %s" % rospy.get_time()
        rospy.loginfo(stat)
        pub.publish(stat)
        rate.sleep()
   
if __name__ == '__main__':
    try:
       talker1()
    except rospy.ROSInterruptException:
        pass
