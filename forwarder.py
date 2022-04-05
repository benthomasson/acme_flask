import os
import json
from flask import Flask, request, jsonify
from azure.servicebus import ServiceBusClient, ServiceBusMessage

app = Flask(__name__)

CONNECTION_STR = os.environ["CONNECTION_STR"]
QUEUE_NAME = os.environ["QUEUE_NAME"]
FORWARDER_NAME = os.environ["FORWARDER_NAME"]


@app.route("/status")
def status():
    return jsonify(dict(status='up'))


@app.route("/<path:endpoint>", methods=["POST", "PUT", "DELETE", "PATCH"])
def webhook(endpoint):
    print(request.headers)
    print(json.dumps(request.json))

    servicebus_client = ServiceBusClient.from_connection_string(
        conn_str=CONNECTION_STR, logging_enable=True
    )

    with servicebus_client:
        sender = servicebus_client.get_queue_sender(queue_name=QUEUE_NAME)
        with sender:
            message = ServiceBusMessage(
                json.dumps(
                    dict(
                        payload=request.json,
                        meta=dict(
                            endpoint=endpoint,
                            headers=dict(request.headers),
                            forwarder=FORWARDER_NAME,
                        ),
                    )
                )
            )
            sender.send_messages(message)

    return "Received", 202
