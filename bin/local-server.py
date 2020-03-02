#!/usr/bin/env python

import os
import sys

PROJECT_PATH = os.path.abspath(os.path.dirname(__name__))
MODULES_PATH = os.path.join(PROJECT_PATH, 'modules')

sys.path.append(PROJECT_PATH)
sys.path.append(os.path.join(MODULES_PATH, 'OSBot-Utils'))

from gw_proxy.local_proxy.Server import Server

print("***** starting local server")
Server(port=12345).setup().start()
