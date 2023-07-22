#!/bin/bash

source .aws_env

aws ecr get-login-password --region "$AWS_REGION" | docker login --username AWS --password-stdin "$AWS_ACCOUNT_ID".dkr.ecr."$AWS_REGION".amazonaws.com
docker pull "$AWS_ACCOUNT_ID".dkr.ecr."$AWS_REGION".amazonaws.com/"$ECR_REPOSITORY":"$IMAGE_TAG"

