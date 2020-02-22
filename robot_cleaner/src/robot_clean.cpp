#include "ros/ros.h"
#include <geometry_msgs/Twist.h>
//method to move robot straight

ros::Publisher vel_pub;

double curr_dist = 0;
void move(double speed, double dist, bool isForward);
using namespace std;

int main(int argc, char **argv)
{
    ros::init(argc, argv, "robot_clean");
    ros::NodeHandle n;
    double speed;
    double distance;
    bool isForward;
    vel_pub = n.advertise<geometry_msgs::Twist>("/turtle1/cmd_vel",10);
    cout<<"enter speed: ";
    cin>>speed;
    cout<<"enter distance: ";
    cin>>distance;
    cout<<"enter forward: ";
    cin>>isForward;
    move(speed,distance,isForward);
}

void move(double speed, double dist, bool isForward)
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
}