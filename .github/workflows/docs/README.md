# Serverless Workshops Platform

This project implements a serverless platform for managing workshops using AWS services.

## Architecture

The system uses the following AWS services:

- Amazon S3 (frontend hosting)
- Amazon CloudFront (CDN)
- Amazon API Gateway
- AWS Lambda
- Amazon DynamoDB
- Amazon Cognito (authentication)

## Features

- Create workshops
- List workshops
- Register users for workshops
- JWT authentication using Cognito

## Deployment

Frontend is deployed using CloudFront and S3.

Backend is implemented using Lambda functions exposed through API Gateway.

Authentication is managed with Amazon Cognito.
