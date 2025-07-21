from venv import create

from bs4 import BeautifulSoup as bs4
import asyncio

class IOParser:

    def __init__(self, html):
        self.html = html

    def __sync_parse(self):
            soup = bs4(self.html, "lxml")
            return len(soup.find_all("div"))

    async def parse(self):
        result = await asyncio.to_thread(self.__sync_parse)
        return result

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        pass