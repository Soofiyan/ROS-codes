#include "ros/ros.h"
#include <geometry_msgs/Twist.h>
#include <turtlesim/Color.h>
//method to move robot straight

ros::Subscriber color_sub;

double curr_dist = 0;
uint8_t r;
uint8_t b;
uint8_t g;
//void move(double speed, double dist, bool isForward);
using namespace std;


void chatterCallback(const turtlesim::Color::ConstPtr& msg)
{
  ROS_INFO("I heard: %d %d %d",msg->r,msg->g,msg->b);

}

int main(int argc, char **argv)
{
    ros::init(argc, argv, "robot_clean");

    ros::NodeHandle n;
    color_sub = n.subscribe("turtle1/color_sensor",10,chatterCallback);

    ros::Rate loop_rate(10);
    loop_rate.sleep();
    /* uint8_t speed;
    uint8_t distance;
    uint8_t isForward;
    vel_pub = n.advertise<geometry_msgs::Twist>("/turtle1/color_sensor",10);
    //move(speed,distance,isForward);
    turtlesim::Color color_sensor;
    color_sensor.r = 100;
    color_sensor.g = 0;
    color_sensor.b = 0;
    vel_pub.publish(color_sensor);
    */
   ros::spin();

   return 0;
}

/*void move(double speed, double dist, bool isForward)
{
    geometry_msgs::Twist vel_msg;
    //distance == speed*time
    if(isForward)
    {
        vel_msg.linear.x = abs(speed);
    }
    else
    {
        vel_msg.linear.x = -abs(speed);
    }
    vel_msg.linear.y = 0;
    vel_msg.linear.z = 0;

    vel_msg.angular.x = 0;
    vel_msg.angular.y = 0;
    vel_msg.angular.z = 0;
    
    //to: current time
    //loop
    //publish the velocity
    //estimate the distance = speed*(t_curr - t_prev)
    //current dist ,oved by robot

    double t0 = ros::Time::now().toSec();
    ros::Rate loop_rate(10);
    while(curr_dist <= dist)
    {
        vel_pub.publish(vel_msg);
        double t1 = ros::Time::now().toSec();
        curr_dist = speed*(t1 - t0);
        ros::spinOnce();
        loop_rate.sleep();
    }
    vel_msg.linear.x = 0;
    vel_pub.publish(vel_msg);
}*/