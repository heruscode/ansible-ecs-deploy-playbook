## Ansible-ecs-deploy-playbook  
  
Use this playbook to deploy a app into Amazon ECS, we use a simple Python app as our default scenario.  
  
This playbook will build the app's image with docker, create and send the image into a ECR repository. Create a VPC and everything that is necessary in it(subnets, security groups...). Create a ELB. Create a EC2 instance. Create a ECS cluster with the service that runs the app's image we created. Your app will be running in seconds.  
  
Make sure you have pip, Docker and Awscli already installed on the computer that will execute this playbook.
  
Make sure you have a AWS account with all permissions necessary to create the services. You will need a AWS Access key ID and AWS Secret Access Key, and a AWS Keypair to configure in the EC2 instance. 

##### How to deploy
1. Insert your AWS credentials with the command ```aws configure```. Also configure your ```Default region name``` with the same region that is set in the file ```ansible/group_vars/all.yml``` in var ``` aws_region```, the default is us-west-2.
2. Insert your AWS keypair in the file ```ansible/group_vars/all.yml```, in var ```aws_keypair``` wich is the name of the keypair that EC2 will use
3. To run the deploy, access the folder ```ansible``` and run the command ```ansible-playbook ansible-ecs-deploy-playbook.yml```.