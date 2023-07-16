#!/bin/bash

source .aws_env

docker tag "${IMAGE_NAME}:${TAG}" "${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com/${ECR_REPOSITORY}:${TAG}"
aws ecr get-login-password --region "$AWS_REGION" | docker login --username AWS --password-stdin $AWS_ACCOUNT_ID.dkr.ecr."$AWS_REGION".amazonaws.com
docker push "$AWS_ACCOUNT_ID".dkr.ecr."$AWS_REGION".amazonaws.com/$ECR_REPOSITORY:$TAG
