# Robot system science Task2   
Multiple display system  　

## Example of use   
tab 1  
`roscore`  

tab 2  
`rosrun mypkg count.py`  
 
tab 3  
`rosrun mypkg multiple.py`  
[INFO] [1609749950.749935]: 16  
2の倍数  
4の倍数  
8の倍数  
16の倍数  
[INFO] [1609749952.750611]: 17  
17の倍数  
[INFO] [1609749954.750584]: 18  
2の倍数  
3の倍数  
6の倍数  
9の倍数  
18の倍数  

tab 4  
`rostopic echo /number`   
data: 4  
data: 1  
data: 5  

### Demo  

#### Operating environment  
OS : Linux20.04.1 LTS  

##### What was used  
Raspberry Pi 4 (8GB)  

###### Usage
`$git clone https://github.com/kentaobata/Robosys_Task2.git`   
 tab 1  
 `roscore`  
 tab 2  
 `rosrun mypkg count.py`  
 tab 3  
 `rosrun mypkg multiple.py`  
 tab 4  
 `rostopic echo /number`  

 
