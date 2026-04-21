# System Architecture

This project implements a serverless workshop management platform using AWS managed services.

## Architecture Overview

The system follows a serverless event-driven architecture.

Client requests flow through a secure API layer, trigger Lambda functions, and persist data in DynamoDB.

### Main Components

Frontend
- Amazon S3 (static website hosting)
- Amazon CloudFront (CDN)

Backend API
- Amazon API Gateway (HTTP API)
- AWS Lambda (serverless compute)
- Amazon DynamoDB (NoSQL database)

Authentication
- Amazon Cognito User Pool
- JWT authorization in API Gateway

Event Driven Components
- Amazon EventBridge
- Amazon SNS notifications

Observability
- Amazon CloudWatch Logs
- Amazon CloudWatch Alarms

Security
- AWS WAF
- IAM least-privilege roles
- Cognito authentication

DevOps
- GitHub Actions CI/CD
- AWS SAM (Infrastructure as Code)

Cost Control
- AWS Budgets

## Architecture Diagram
