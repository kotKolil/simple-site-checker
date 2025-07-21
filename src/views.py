from json.decoder import JSONArray

from aiohttp import web
import aiofiles
from src.requests import IOClient
from src.parser import IOParser
from asynclogger import logger
import json

logger.config("")

async def root(request):
    async with aiofiles.open("src/templates/index.html", "r") as page:
        await logger.info('request to index page')
        return web.Response(text= await page.read(), content_type='text/html')

async def client(request):
    async with IOClient(request.match_info["uri"]) as request:
        await request.get()
        text = str(request.document)
        parser = IOParser(text)
        result = await parser.parse()
        return  web.Response(text = json.dumps({
            "divNum": result
        }), content_type="application/json")

