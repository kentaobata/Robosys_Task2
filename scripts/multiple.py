#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

n = 0
num = 0
multi = 0

def callback(message):
    global n
    global num
    global nulti

    n = message.data

    rospy.loginfo(message.data)
    num = 0
    for multi in range(2, 50):
        if n % multi == 0:
            print('%dの倍数' % multi)
            num += 1

if __name__ == '__main__':
    rospy.init_node('number')
    sub = rospy.Subscriber('count_up', Int32, callback)
    pub = rospy.Publisher('number', Int32, queue_size=1)
    rate = rospy.Rate(0.5)
    while not rospy.is_shutdown():
            pub.publish(num)
            rate.sleep()


