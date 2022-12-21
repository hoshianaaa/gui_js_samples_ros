#!/usr/bin/env python

import rospy
from std_msgs.msg import *
from geometry_msgs.msg import *

# ps_mgs, parameter
# planner, editor, calibration2

data = "parameter,editor" 

initial_param = {'param1': "ps_mgs,planner"}
param = {'param1': "ps_mgs,planner"}

def callback(msg):
  global data
  print(msg.data)
  data = msg.data

  #########################
  print(type(data))
  param['param1'] = data
  update_file()
  ########################


###########################################
import json
import os

def read_json_file(file_name):
  if os.path.exists(file_name):
    with open(file_name, 'r') as f:
      json_load = json.load(f)
      return json_load, True
  return None, False

def write_json_file(file_name, dict_data):
  with open(file_name, 'w') as f:
    json.dump(dict_data, f, indent=2)

def initialize_file():
  global initial_param
  global f_name
  write_json_file(f_name, initial_param)

def update_file():
  global param
  global f_name
  write_json_file(f_name, param)

project = "gui_js_samples"
node_name = "web_state"

rospy.init_node(node_name)

f_name = os.environ['HOME'] + "/.ros/" + project + "-" +  node_name + "-params.json"

file_data, read_sucess = read_json_file(f_name)
if read_sucess == False:
  initialize_file()
else:
  try:
    data = file_data['param1']
    print(data)
  except:
    initialize_file()
##########################################

pub = rospy.Publisher("browser/state", String, queue_size=10)
sub = rospy.Subscriber("browser/set_state", String, callback)

r = rospy.Rate(100)

while not rospy.is_shutdown():
  pub.publish(String(data))
  r.sleep()
