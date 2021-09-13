Steps for AWS Configuration using Boto3 and AWS client via Python in local machine:

1. Download VSCode and install Boto3, awscli using pip.
2. Download the keycode from the AWS Management console
3. We need to create a user in IAM. - https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html#id_users_create_console
4. Get the access key ID and Secret Key ID
5. Insert these using -- aws configuration on your vscode command line. Insert location as well (eg: us-east-1)
6. In the py code, after importing boto3 and creating the client, we need AMI ID to run the instance via the boto3 client. So, look for it on AWS Management Console
7. We can find AMI Instance by clicking on 'launch instances' in EC2 section - Eg: ami-087c17d1fe0178315. This is AMI of Amazon Linux 2 AMI.
NOTE: AMI Ids vary with locations. Please make sure if these match.
8. We want key name too. If we want to know our key pair existing ones, search for "Key Pair" on AWS console. and select Key Pair feature. We can use one of them. If we wanna create one, we can too.
9. Code the client to start, and get description, and reboot
10. Quit
