#!/bin/bash

# source .aws_env

docker tag "${IMAGE_NAME}:${TAG}" "${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com/${ECR_REPOSITORY}:${TAG}"

