#!/usr/bin/env python
import rospy
from automa.msg import smoke_sensor
#import Jeston.GPIO as GPIO
#import time

input_pin = 18  #Board pin 12   

# prev_value = None
# GPIO.setmode(GPIO.BCM)  # BCM pin-numbering scheme from Raspberry Pi
# GPIO.setup(input_pin, GPIO.IN)  # set pin as an input pin

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

# def sensor_pub():
#     value = GPIO.input(input_pin)
#     if value != prev_value:
#         if value == GPIO.HIGH:
#             value_str = "HIGH"
#         else:
#             value_str = "LOW"
#         print("Value read from pin {} : {}".format(input_pin,
#                                                     value_str))
#         prev_value = value
#     time.sleep(1)


if __name__ == '__main__':
    try:
        while not rospy.is_shutdown():
            publish_smoke_val()
    except rospy.ROSInterruptException:
        pass
    # finally:
    #     GPIO.cleanup()