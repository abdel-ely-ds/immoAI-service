#!/bin/bash

source .aws_env

# Use the environment variables in the docker tag command
docker tag "${IMAGE_NAME}:${TAG}" "${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com/${ECR_REPOSITORY}:${TAG}"
# shellcheck disable=SC2086
aws ecr get-login-password --region "$AWS_REGION" | docker login --username AWS --password-stdin $AWS_ACCOUNT_ID.dkr.ecr."$AWS_REGION".amazonaws.com

# shellcheck disable=SC2086
docker push "$AWS_ACCOUNT_ID".dkr.ecr."$AWS_REGION".amazonaws.com/$ECR_REPOSITORY:$TAG
