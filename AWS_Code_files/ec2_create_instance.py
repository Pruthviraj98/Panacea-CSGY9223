import boto3

def create_instance_ec2():
    try:
        print("Creating the EC2 Instance")
        #create a client using boto3
        ec2_resource=boto3.client("ec2")
        #now we have to run a prticular instance using this client
        ec2_resource.run_instances(
            #imageid = AMI ID
            ImageId="ami-087c17d1fe0178315",
            #we want to have a Max and min amount of count of instances
            MinCount=1,
            MaxCount=1,
            #creating instance type
            InstanceType="t2.micro",
            #for SHA encryption
            KeyName="ninja_key_virginia"
            #we can also give VPC, subnet IDs, and Security Groups here itself. 
        )#here we have to give the aws access keys and secret keys here as a parameters. But we have already done it in the cli. So, no need to do this again
    except Exception as e:
        print(e)
    
def get_instance_description():
    try:
        print("Describe the EC2 Instance that are created")
        #create a client using boto3
        ec2_resource=boto3.client("ec2")
        #now we have to describe a prticular instance using this client
        description=ec2_resource.describe_instances()
        #manually get info by the cli by printing description or get the required info like this as coded below
        #in case of multiple instances, to select only one instance, use: ec2_resource.describe_instances(instance_ids=["TYPE-INSTANCE-ID-HERE"])
        Reservations=description["Reservations"][0]
        Instances=Reservations['Instances'][0]
        # ret=[Instances['PrivateIpAddress'], Instances['PublicIpAddress'], Instances['InstanceId']]
        ret=str(Instances["InstanceId"])
        return ret
    except Exception as e:
        print(e)

def reboot_ec2_instance():
    try:
        print("Reboot the EC2 Instances")
        #create a client using boto3
        ec2_resource=boto3.client("ec2")
        #now we have to reboot a prticular instance using this client
        instance_name=get_instance_description()
        ec2_resource.reboot_instances(InstanceIds=[instance_name])
        print("Instance with instance Name: "+instance_name+" has been rebooted")
    except Exception as e:
        print(e)

def stop_ec2_instance():
    try:
        print("Stop the EC2 Instances")
        #create a client using boto3
        ec2_resource=boto3.client("ec2")
        #now we have to stop a prticular instance using this client
        instance_name=get_instance_description()
        ec2_resource.stop_instances(InstanceIds=[instance_name])
        print("Instance with instance Name: "+instance_name+" has been stopped")
    except Exception as e:
        print(e)

def start_ec2_instance():
    try:
        print("Start the EC2 Instances")
        #create a client using boto3
        ec2_resource=boto3.client("ec2")
        #now we have to start a prticular instance using this client
        instance_name=get_instance_description()
        ec2_resource.start_instances(InstanceIds=[instance_name])
        print("Instance with instance Name: "+instance_name+" has been started")
    except Exception as e:
        print(e)

# create_instance_ec2()
# reboot_ec2_instance()
# print(get_instance_description())
# stop_ec2_instance()
# start_ec2_instance()
