# Robot system science Task2   
Divisor program 　

# Example of use     

tab 3  
`rosrun mypkg multiple.py` : Shows divisors of numbers increasing by 1  

[INFO] [1609763058.569654]: 241  
素数  
[INFO] [1609763060.571186]: 242   　　
2の倍数　　  
11の倍数　　  
22の倍数　　  
121の倍数　　  
[INFO] [1609763062.571217]: 243　　  
3の倍数　　  
9の倍数　　  
27の倍数　　  
81の倍数　　  

tab 4  
`rostopic echo /number`　: Show the number of divisors of each number  

data: 0  
data: 4  
data: 4    　

# Demo  
https://youtu.be/UuXclInOQUw

# Operating environment  
OS : Linux20.04.1 LTS  

# What was used  
Raspberry Pi 4 (8GB)  

# Usage
`$https://github.com/kentaobata/Robosys_Task2.git`   
 tab 1  
 `$roscore`  
 tab 2  
 `$rosrun mypkg count.py`  
 tab 3  
 `$rosrun mypkg multiple.py`  
 tab 4  
 `$rostopic echo /number`  
 
 # Licence  
 BSD 3-Clause License  
 
 # Reference
 https://github.com/ryuichiueda/ros_setup_scripts_Ubuntu20.04_server.git
 
 

 
