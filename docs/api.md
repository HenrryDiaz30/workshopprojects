# API Endpoints

Base URL

https://<api-id>.execute-api.us-east-1.amazonaws.com/prod

Authentication uses Amazon Cognito with JWT tokens.

Authorization header example

Authorization: Bearer <JWT_TOKEN>

---

## GET /workshops

Returns a list of available workshops.

Response

200 OK

[
{
"id": "w1",
"title": "Cloud Fundamentals",
"capacity": 30
}
]

---

## POST /workshops

Creates a new workshop.

Request

{
"title": "AWS Serverless",
"capacity": 20
}

Response

201 Created

{
"message": "Workshop created"
}

---

## POST /workshops/{id}/register

Registers a student to a workshop.

Request

{
"userId": "123"
}

Response

200 OK

{
"message": "Registration successful"
}

This endpoint also emits an event to EventBridge.
