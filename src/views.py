from aiohttp import web
import aiofiles
from src.requests import Client
from asynclogger import logger

logger.config("")

async def root(request):
    async with aiofiles.open("src/templates/index.html", "r") as page:
        await logger.info('request to index page')
        return web.Response(text= await page.read(), content_type='text/html')

async def client(request):
    async with Client(request.match_info["uri"]) as response:
        return web.Response(text = str(response.ok))
