#!/usr/bin/env python

import os
import sys

PROJECT_PATH = os.path.abspath(os.path.dirname(__name__))
MODULES_PATH = os.path.join(PROJECT_PATH, 'modules')

sys.path.append(PROJECT_PATH)
sys.path.append(os.path.join(MODULES_PATH, 'OSBot-Utils'))

from gw_proxy.local_proxy.Server import Server

if len(sys.argv) == 1:
    target_server = 'https://httpbin.org'
else:
    target_server = sys.argv[1]

port=12345

print(f'***** starting proxy server for url: {target_server} on port {port}')
Server(target=target_server, port=port).setup().start()
