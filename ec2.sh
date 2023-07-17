#!/bin/bash

# source .aws_env

EXISTING_INSTANCE=$(aws ec2 describe-instances \
  --filters "Name=tag:Name,Values=$APP_NAME" "Name=instance-state-name,Values=running" \
  --query 'Reservations[0].Instances[0].InstanceId' \
  --output text
)

if [ -z "$EXISTING_INSTANCE" ] || [ "$EXISTING_INSTANCE" = "None" ]; then
  INSTANCE_INFO=$(aws ec2 run-instances \
    --image-id "$AMI_ID" \
    --instance-type "$INSTANCE_TYPE" \
    --region "$AWS_REGION" \
    --tag-specifications "ResourceType=instance,Tags=[{Key=Name,Value=$APP_NAME}]" \
    --output json
  )

  INSTANCE_ID=$(echo "$INSTANCE_INFO" | grep -o '"InstanceId": "[^"]*' | awk -F ': "' '{print $2}')

  aws ec2 wait instance-running --instance-ids "$INSTANCE_ID" --region "$AWS_REGION"

  PUBLIC_IP=$(aws ec2 describe-instances --instance-ids "$INSTANCE_ID" --query 'Reservations[0].Instances[0].PublicIpAddress' --output text --region "$AWS_REGION")

  echo "EC2 instance created successfully!"
  echo "Instance ID: $INSTANCE_ID"
  echo "Public IP: $PUBLIC_IP"

else
  INSTANCE_ID="$EXISTING_INSTANCE"
  PUBLIC_IP=$(aws ec2 describe-instances --instance-ids "$INSTANCE_ID" --query 'Reservations[0].Instances[0].PublicIpAddress' --output text --region "$AWS_REGION")

  echo "An EC2 instance with Name=$APP_NAME is already running!"
  echo "Instance ID: $INSTANCE_ID"
  echo "Public IP: $PUBLIC_IP"
fi
