#!/usr/bin/env python
import rospy
from automa.msg import smoke_sensor

pub = rospy.Publisher('smoke_sensor_topic',smoke_sensor, queue_size = 10)
rospy.init_node('sensor_pub_node', anonymous=True)
r = rospy.Rate(1)
value = 0

def publish_smoke_val():
    global value
    value = value ^ 1
    msg = smoke_sensor()
    msg.smoke_val = value
    # rospy.loginfo("Smoke_sensor_value : ")
    # rospy.loginfo(msg)
    pub.publish(msg)
    print(msg)
    r.sleep()

try:
    while not rospy.is_shutdown():
        publish_smoke_val()
except rospy.ROSInterruptException:
    pass