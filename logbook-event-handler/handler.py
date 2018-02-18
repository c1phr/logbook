import os
import boto3
from flask import Flask, jsonify, request
from events.aircraft_seen_event import AircraftSeenEvent

app = Flask(__name__)

EVENTS_TABLE = os.environ['EVENTS_TABLE']
IS_OFFLINE = os.environ.get('IS_OFFLINE')

if IS_OFFLINE:
    client = boto3.client(
        'dynamodb',
        region_name='localhost',
        endpoint_url='http://localhost:8000'
    )
else:
    client = boto3.client('dynamodb')


@app.route('/')
def get_events():
    return jsonify(client.scan(TableName=EVENTS_TABLE))


@app.route("/", methods=["POST"])
def intake_event():
    if request.json.get('type') == 'AircraftSeenEvent':
        event = AircraftSeenEvent.fromJson(request.json)
        savedEvent = client.put_item(
            TableName=EVENTS_TABLE,
            Item=event.to_dynamo()
        )
        return jsonify(event.serialize())
    else:
        return jsonify("Event type " + request.json.get('type') + " unsupported!")