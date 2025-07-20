import aiohttp
from asynclogger import logger


class Client:

    def __init__(self, url):
        self.url = url

    async def get(self):
        try:
            self.client =  aiohttp.ClientSession()
            self.response = await self.client.get(self.url)
            await logger.info(f"request to {self.url} successful")
            self.ok = self.response.ok
            await self.response.release()
            await self.client.close()

        except Exception as e:
            await logger.info(f"request to {self.url} failed")
            self.ok = False
            self.exception = str(e)



    async def __aenter__(self):
        try:
            self.client =  aiohttp.ClientSession()
            self.response = await self.client.get(self.url)
            await logger.info(f"request to {self.url} successful")
            self.ok = self.response.ok
            return self

        except Exception as e:
            await logger.info(f"request to {self.url} failed")
            self.ok = False
            self.exception = str(e)
            return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.ok:
            await self.response.release()
            await self.client.close()