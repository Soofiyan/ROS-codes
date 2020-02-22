#include "ros/ros.h"
#include "automa/smoke_sensor.h"

void chatterCallback(const automa::smoke_sensor::ConstPtr& msg)
{
  ROS_INFO("I heard from sensor_pub: %d",msg->smoke_val);
}

void chatterCallback1(const automa::smoke_sensor::ConstPtr& msg)
{
  ROS_INFO("I heard from talker: %d",msg->smoke_val);
}

int main(int argc, char **argv)
{
  ros::init(argc, argv, "sensor_receive_node");
  ros::NodeHandle n;
  ros::Subscriber sub = n.subscribe("smoke_sensor_topic", 1000, chatterCallback);
  ros::Subscriber sub1 = n.subscribe("chatter", 1000, chatterCallback1);
  ros::spin();
  return 0;
}
