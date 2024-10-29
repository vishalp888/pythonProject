import boto3

client = boto3.client('ec2')
response = client.run_instances(
ImageId='ami-04a37924ffe27da53',
    InstanceType='t2.micro',
KeyName='awsaws')
