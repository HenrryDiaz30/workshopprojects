import json
import boto3
from datetime import datetime, timezone

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('workshops')

def lambda_handler(event, context):
    try:
        body = json.loads(event.get("body", "{}"))

        workshop_id = body.get("id")
        name = body.get("name")
        description = body.get("description", "")
        category = body.get("category", "")
        location = body.get("location", "")
        start_at = body.get("startAt", "")
        end_at = body.get("endAt", "")
        capacity = body.get("capacity", 0)

        if not workshop_id or not name:
            return {
                "statusCode": 400,
                "headers": {
                    "Content-Type": "application/json",
                    "Access-Control-Allow-Origin": "*"
                },
                "body": json.dumps({"message": "id y name son obligatorios"})
            }

        now = datetime.now(timezone.utc).isoformat()

        item = {
            "PK": f"WORKSHOP#{workshop_id}",
            "SK": "META",
            "name": name,
            "description": description,
            "category": category,
            "location": location,
            "startAt": start_at,
            "endAt": end_at,
            "status": "scheduled",
            "capacity": capacity,
            "createdAt": now,
            "updatedAt": now
        }

        table.put_item(Item=item)

        return {
            "statusCode": 201,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps({
                "message": "Taller creado correctamente",
                "item": item
            })
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps({"message": str(e)})
        }