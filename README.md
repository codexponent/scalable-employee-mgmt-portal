# Scalable Employee Mgmt Portal
Scalable Employee Management Portal

# Motivation:
In today's world, our application should be able to handle multiple requests from customers all around the world. So it is important to make an application fault-tolerant and able to scale as the need of the demand. This post talks about how to create a scalable web application using various AWS services like Load Balancers, Target Groups, Auto Scaling, Launch Configuration, Amazon Machine Image(AMI), Route 53, and so on.

# Architecture:
![architecture](https://user-images.githubusercontent.com/13358738/123594750-d257a380-d80f-11eb-9549-ba81fa0b3b36.png)

# Prerequisites:
1. AWS EC2
2. AWS AMI
3. Load Balancer
4. Auto Scaling Groups
5. MySQL Instance
6. Route 53

# Replication Steps:
1. Create a config.ini file
```bash
[MYSQL]
user=
password=
host=
database=
```
2. Commands to confgure the application
```bash
git clone git@github.com:codexponent/scalable-employee-mgmt-portal.git
pip install -r requirements.txt
python main.py
```
3. Create a reboot cronjob for the AMI Image
```bash
touch run.sh
echo "#!/bin/bash 
python main.py" > run.sh

crontab -e
@reboot /home/ec2-user/scalable-employee-mgmt-portal/run.sh
```
4. Start to create AMI Image written on the post.
