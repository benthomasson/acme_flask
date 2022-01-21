#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Usage:
    forwarder [options]

Options:
    -h, --help        Show this page
    --debug            Show debug logging
    --verbose        Show verbose logging
"""
from docopt import docopt
import logging
import os
import sys
import json
from flask import Flask, request
from azure.servicebus import ServiceBusClient, ServiceBusMessage

logger = logging.getLogger('forwarder')


app = Flask(__name__)

CONNECTION_STR = os.environ['CONNECTION_STR']
QUEUE_NAME = os.environ['QUEUE_NAME']


@app.route('/', methods=['POST'])
def webhook():
    print(json.dumps(request.json))

    servicebus_client = ServiceBusClient.from_connection_string(conn_str=CONNECTION_STR, logging_enable=True)

    with servicebus_client:
        sender = servicebus_client.get_queue_sender(queue_name=QUEUE_NAME)
        with sender:
            message = ServiceBusMessage(json.dumps(request.json))
            sender.send_messages(message)

    return 'Received', 202


def main(args=None):
    if args is None:
        args = sys.argv[1:]
    parsed_args = docopt(__doc__, args)
    if parsed_args['--debug']:
        logging.basicConfig(level=logging.DEBUG)
    elif parsed_args['--verbose']:
        logging.basicConfig(level=logging.INFO)
    else:
        logging.basicConfig(level=logging.WARNING)

    app.run(host='0.0.0.0', port='8000')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
