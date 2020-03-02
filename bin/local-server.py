#!/usr/bin/env python

import os
import sys

PROJECT_PATH = os.path.abspath(os.path.dirname(__name__))
MODULES_PATH = os.path.join(PROJECT_PATH, 'modules')

sys.path.append(PROJECT_PATH)
sys.path.append(os.path.join(MODULES_PATH, 'OSBot-Utils'))

from gw_proxy.local_proxy.Server import Server

target_server = 'https://httpbin.org'
port          = 12345

if len(sys.argv) == 2:
    target_server = sys.argv[1]
elif len(sys.argv)==3:
    target_server = sys.argv[1]
    port          = int(sys.argv[2])



print(f'***** starting proxy server for url: {target_server} on port {port}')
Server(target=target_server, port=port).setup().start()



# https://www.transfernow.net
# https://www.projectsend.org
# https://www.dropsend.com
# https://transferxl.com
# https://www.sendfiles.net
# https://free.mailbigfile.com/
# https://www.justbeamit.com/  (very interresting concept)
# https://www.sendspace.com/

# https://demo1.nextcloud.com
