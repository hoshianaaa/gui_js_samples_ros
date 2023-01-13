# gui_js_samples_ros
javascript ros samples

## install

```
cd ~/catkin_ws/src
git clone https://github.com/hoshianaaa/gui_js_samples_ros.git
catkin build
source ~/catkin_ws/devel/setup.bash
```

## run

```
roscd gui_js_samples_ros
bash run
```

## app

- `graph.html`

```
roslaunch  gui_js_samples_ros graph.launch
```

```
on click graph publish topic : 'Geometry_msgs/PoseStamped'
subscribe topic and show graph : 'Geometry_msgs/PoseStamped'
```
![Screenshot from 2022-12-19 18-55-04](https://user-images.githubusercontent.com/40942409/208398328-c773e8ab-7cda-4f8b-b768-789bcd8fb437.png)
