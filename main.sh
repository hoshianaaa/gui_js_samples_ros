#python3 -m http.server &

#google-chrome http://localhost:8000
#firefox http://localhost:8000 &

SCRIPT_DIR=$(cd $(dirname $0); pwd)
WS=catkin_ws

echo " - ros server"
gnome-terminal --tab -t "rosbridge server" -- bash -c "source /opt/ros/*/setup.bash; source $HOME/$WS/devel/setup.bash; roslaunch  gui_js_samples_ros main.launch; exec bash"

echo " - http server"
gnome-terminal --tab -t "http server" -- bash -c "cd $SCRIPT_DIR/webpages; python3 -m http.server 8004; exec bash"

sleep 2

echo " - google-chrome"
gnome-terminal -- bash -c "google-chrome http://localhost:8004"
