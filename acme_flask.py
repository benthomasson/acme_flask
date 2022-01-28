#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Usage:
    acme_flask [options]

Options:
    -h, --help        Show this page
    --debug            Show debug logging
    --verbose        Show verbose logging
"""
from docopt import docopt
import logging
import sys
from flask import Flask, send_from_directory
from acme_tiny import get_crt
import multiprocessing as mp

logger = logging.getLogger('forwarder')


app = Flask(__name__)

CHALLENGE_FOLDER = 'challenges'


@app.route("/.well-known/acme-challenge/<path:name>")
def download_file(name):
    return send_from_directory(CHALLENGE_FOLDER, name)


def get_and_write_crt(account_key, csr, challenge_folder, crt_file):
    signed_crt = get_crt(account_key, csr, challenge_folder)
    with open(crt_file, 'w') as f:
        f.write(signed_crt)


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

    flask_server = mp.Process(target=app.run,
                              kwargs=dict(host='0.0.0.0', port='80'))
    flask_server.daemon = True
    flask_server.start()

    acme_request = mp.Process(target=get_and_write_crt, args=('account.key',
                                                              'domain.csr',
                                                              CHALLENGE_FOLDER,
                                                              'acme/server.crt'))
    acme_request.start()
    acme_request.join()

    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
