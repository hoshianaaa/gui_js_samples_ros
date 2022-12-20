#!/usr/bin/env python

import rospy
from std_msgs.msg import *
from geometry_msgs.msg import *
from nav_msgs.msg import *
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

def gen_pose_stamped(x,y,angle,frame_id = "map"):

  pose = PoseStamped()
  #pose.header.frame_id = frame_id
  pos = Point()
  quat = Quaternion()

  euler = Vector3()
    
  pos.x = x
  pos.y = y
  pos.z = 0

  euler.z = angle

  pose.pose.position = pos
  pose.pose.orientation = euler_to_quaternion(euler) 

  return pose


rospy.init_node("pub_path")
pub = rospy.Publisher("~data", Path, queue_size=10)

r = rospy.Rate(10)

msg = Path()
msg.header.frame_id = "map"
msg.poses.append(gen_pose_stamped(1,1,0))
msg.poses.append(gen_pose_stamped(1,3,0))
msg.poses.append(gen_pose_stamped(3,3,0))
msg.poses.append(gen_pose_stamped(3,1,0))

while not rospy.is_shutdown():

  print(msg)

  pub.publish(msg)
  r.sleep()
