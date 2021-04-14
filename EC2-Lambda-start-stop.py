#this lambda function will automatically start/stop the instances

import json
import boto3

#Change region as per choice
region = 'us-east-1'


ec2 = boto3.client('ec2', region_name = region)

def lambda_handler(event, context):
    instances = event["instances"].split(",")
    action = event["action"]
    
    if action == 'Start':
        print('Starting your instances: ' + str(instances))
        ec2.start_instances(InstanceIds = instances)
        response = 'Successfully started instance' + str(instances)
    elif action == 'Stop':
        print('Stopping your instances: ' + str(instances))
        ec2.stop_instances(InstanceIds = instances)
        response = 'Successfully stopped instance' + str(instances)
    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }

#after this, set event CONFIGURE TEST EVENTS and set the following below
#{
#  "instances": "i-07a4cf02c,i-0290ad7793,instance ids seperated by comma",
#  "action": "Stop" or "Start"
#}
