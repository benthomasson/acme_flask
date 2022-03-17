
# Webhook Forwarder

This project provides a service to receive any incoming webhook and forward it to an Azure service bus.
This is useful if you do not want to open a port to host a webhook in your infrastructure.  Instead
you can connect to the Azure service bus and handled the queued messages.

The headers, body, and path of the webhook call are captured a JSON data structure that is then
inserted into the event.

The structure of the event is as follows:

    {'payload': <body of the webhook call>,
     'meta': {'endpoint': <API endpoint called>
              'headers': <HTML headers>,
              'forwarder-name': <the name of this webhook forwarder>}}


The service uses Let's Encrypt to provide https certificates on Azure.
