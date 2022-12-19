#!/usr/bin/env python

import rospy
from std_msgs.msg import *
from geometry_msgs.msg import *
import math
import tf

DEG_TO_RAD = math.pi / 180
RAD_TO_DEG = 180 / math.pi

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

rospy.init_node("pub_pose")
pub = rospy.Publisher("~data", PoseStamped, queue_size=10)

r = rospy.Rate(10)

msg = PoseStamped()
msg.header.frame_id = "map"
pos = Point()
quat = Quaternion()

euler = Vector3()
euler.z = 30 * DEG_TO_RAD
pos.x = 0

while not rospy.is_shutdown():
  
  pos.x = pos.x + 0.03
  if pos.x > 3:
    pos.x = 0
  pos.y = 2
  pos.z = 0

  euler.z = euler.z + 10 * DEG_TO_RAD

  msg.pose.position = pos

  msg.pose.orientation = euler_to_quaternion(euler) 

  print(msg)

  pub.publish(msg)
  r.sleep()
