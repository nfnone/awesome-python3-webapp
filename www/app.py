# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 10:43:15 2019

@author: ASUS
"""
import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web

async def index(request):
    return web.Response(body='<h1>Awesome</h1>'.encode('utf-8'),content_type="text/html")

def init():
    app = web.Application()
    app.add_routes([web.get('/', index)])
    web.run_app(app, host='127.0.0.1', port=9000)
# =============================================================================
#     app = web.Application(loop=loop)
#     app.router.add_route('GET', '/', index)
#     srv = yield from loop.create_server(app.make_handler(), '127.0.0.1', 9000)
# =============================================================================
    logging.info('server started at http://127.0.0.1:9000...')
# =============================================================================
# loop = asyncio.get_event_loop()
# loop.run_until_complete(init(loop))
# loop.run_forever()
# =============================================================================
init()








