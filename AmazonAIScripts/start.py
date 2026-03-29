#Copyright 2020 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-custom-labels-developer-guide/blob/master/LICENSE-SAMPLECODE.)

import boto3
from botocore.config import Config
from dotenv import load_dotenv

def start_model(project_arn, model_arn, version_name, min_inference_units):
    load_dotenv()
    
    my_config = Config(
        region_name="us-east-2"
    )
    client=boto3.client('rekognition', config=my_config)

    try:
        # Start the model
        print('Starting model: ' + model_arn)
        response=client.start_project_version(ProjectVersionArn=model_arn, MinInferenceUnits=min_inference_units)
        # Wait for the model to be in the running state
        project_version_running_waiter = client.get_waiter('project_version_running')
        project_version_running_waiter.wait(ProjectArn=project_arn, VersionNames=[version_name])

        #Get the running status
        describe_response=client.describe_project_versions(ProjectArn=project_arn,
            VersionNames=[version_name])
        for model in describe_response['ProjectVersionDescriptions']:
            print("Status: " + model['Status'])
            print("Message: " + model['StatusMessage']) 
    except Exception as e:
        print(e)
        
    print('Done...')
    
def main():
    project_arn='arn:aws:rekognition:us-east-2:339713114793:project/flowers_classification/1709394025366'
    model_arn='arn:aws:rekognition:us-east-2:339713114793:project/flowers_classification/version/flowers_classification.2024-03-02T15.03.06/1709409787112'
    min_inference_units=1 
    version_name='flowers_classification.2024-03-02T15.03.06'
    start_model(project_arn, model_arn, version_name, min_inference_units)

if __name__ == "__main__":
    main()