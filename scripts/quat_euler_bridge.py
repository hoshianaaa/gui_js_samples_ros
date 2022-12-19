#!/usr/bin/env python

import rospy
from std_msgs.msg import *
from geometry_msgs.msg import *
import tf

def euler_to_quaternion(euler):
    """Convert Euler Angles to Quaternion

    euler: geometry_msgs/Vector3
    quaternion: geometry_msgs/Quaternion
    """
    q = tf.transformations.quaternion_from_euler(euler.x, euler.y, euler.z)
    return Quaternion(x=q[0], y=q[1], z=q[2], w=q[3])

def quaternion_to_euler(quaternion):
    """Convert Quaternion to Euler Angles

    quarternion: geometry_msgs/Quaternion
    euler: geometry_msgs/Vector3
    """
    e = tf.transformations.euler_from_quaternion((quaternion.x, quaternion.y, quaternion.z, quaternion.w))
    return Vector3(x=e[0], y=e[1], z=e[2])

def callback(msg):
  global pub
  print(msg)

  quat = msg.pose.orientation
  euler = quaternion_to_euler(quat)

  pub_msg = PoseStamped()
  pub_msg = msg
  pub_msg.pose.orientation.x = euler.x
  pub_msg.pose.orientation.y = euler.y
  pub_msg.pose.orientation.z = euler.z
  pub_msg.pose.orientation.w = 0

  pub.publish(pub_msg)

rospy.init_node("quat_euler_bridge")
pub = rospy.Publisher("/pub_pose/data_euler", PoseStamped, queue_size=10)
rospy.Subscriber("/pub_pose/data", PoseStamped, callback)

r = rospy.Rate(10)

while not rospy.is_shutdown():
  r.sleep()
