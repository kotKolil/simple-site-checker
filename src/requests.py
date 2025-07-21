import aiohttp
from asynclogger import logger


class IOClient:

    def __init__(self, url):
        self.document = None
        self.url = url

    async def get(self):
        try:
            self.client =  aiohttp.ClientSession()
            self.response = await self.client.get(self.url)
            await logger.info(f"request to {self.url} successful")
            self.ok = self.response.ok
            self.document = await self.response.read()
            await self.response.release()
            await self.client.close()

        except Exception as e:
            await logger.info(f"request to {self.url} failed")
            self.ok = False
            self.exception = str(e)



    async def __aenter__(self):
            return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        pass