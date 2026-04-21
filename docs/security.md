# Security

Security is implemented across multiple layers.

## Authentication

Amazon Cognito User Pool manages user authentication.

JWT tokens are validated by API Gateway.

## Authorization

Protected endpoints require a valid JWT token.

Public endpoints include:

GET /workshops

## Web Application Firewall

AWS WAF protects the API against common web attacks.

Rule set:

AWS Core Rule Set

Protection includes:

- SQL injection
- Cross-site scripting
- malicious request patterns

## IAM

Lambda functions use IAM roles with least-privilege permissions.

Example permissions:

- DynamoDB access
- EventBridge event publishing
