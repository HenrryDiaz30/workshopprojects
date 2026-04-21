# Deployment

Infrastructure is defined using AWS SAM.

## Prerequisites

- AWS CLI
- AWS SAM CLI
- Git
- Node.js

## Build Infrastructure

Inside the infra directory:

sam build

## Deploy Infrastructure

sam deploy --guided

This command creates:

- API Gateway
- Lambda functions
- DynamoDB table
- EventBridge configuration

## CI/CD

CI/CD is implemented using GitHub Actions.

Pipeline steps:

1. Checkout repository
2. Configure AWS credentials
3. Upload frontend to S3
4. Invalidate CloudFront cache

Pipeline file:

.github/workflows/deploy.yml
