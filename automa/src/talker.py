#!/usr/bin/env python
import rospy
from automa.msg import smoke_sensor

def talker():
    pub = rospy.Publisher('chatter', smoke_sensor, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(1) # 10hz
    value = 0
    while not rospy.is_shutdown():
        value = value + 1
        msg = smoke_sensor()
        msg.smoke_val = value
        hello_str = "hello world %s" % rospy.get_time()
        print(msg)
        # rospy.loginfo(msg)
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
