# Observability

The platform uses AWS native monitoring tools.

## Logging

All Lambda functions send logs to CloudWatch Logs.

Log group example

/aws/lambda/registerWorkshop

## Metrics

CloudWatch automatically tracks:

- Lambda invocations
- Lambda errors
- API Gateway latency
- DynamoDB capacity usage

## Alarms

Example alarm configured:

lambda-register-errors

Triggers when errors > 1 within 5 minutes.

Notifications are sent via SNS.

## Event Monitoring

EventBridge is used to emit domain events such as:

STUDENT_REGISTERED
