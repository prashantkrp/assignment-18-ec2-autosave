import json
import boto3

ec2 = boto3.client('ec2')

def lambda_handler(event, context):
    print("Event:", json.dumps(event))

    instance_id = event['detail']['instance-id']

    volumes = ec2.describe_instances(InstanceIds=[instance_id])

    for reservation in volumes['Reservations']:
        for instance in reservation['Instances']:
            for mapping in instance['BlockDeviceMappings']:
                volume_id = mapping['Ebs']['VolumeId']

                ec2.create_snapshot(
                    VolumeId=volume_id,
                    Description=f"Backup of {volume_id} before shutdown"
                )

    return {
        'statusCode': 200,
        'body': 'Snapshot created'
    }
