# assignment1
 ROS1 assignment
 
# Run instructions
[Terminal 1]
```
git clone https://github.com/Mlahoud/assignment1.git
cd assignment1
chmod +x src/assignment_scripts/scripts/randPos_service.py
chmod +x src/assignment_scripts/scripts/reply_node.py
chmod +x src/assignment_scripts/scripts/srvCaller_node.py
git clone -b noetic https://github.com/CarmineD8/robot_description.git src/robot_description
git checkout noetic
catkin_make
source devel/setup.bash
roslaunch assignment_scripts assignment.launch 
```
