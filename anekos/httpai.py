"""Async Nekos.life API interactor

MIT License

Copyright (c) 2022 EgorBron

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import aiohttp
try:
    import ujson as json
except ImportError:
    import warnings
    warnings.warn("ujson library not found, standard lib will be used, operations with json may be a bit slower")
    del warnings
    import json

class NekosAsyncAPI:
    def __init__(self, base_url):
        self.base_url = base_url

    async def get(self, url, **kwargs):
        async with aiohttp.ClientSession(json_serialize=json) as session:
            async with session.get(self.base_url+url, **kwargs) as resp:
                return resp

    async def post(self, url, **kwargs):
        async with aiohttp.ClientSession(json_serialize=json) as session:
            async with session.post(self.base_url+url, **kwargs) as resp:
                return resp

    async def get_as_json(self, url, **kwargs):
        async with aiohttp.ClientSession(json_serialize=json) as session:
            async with session.get(self.base_url+url, **kwargs) as resp:
                return await resp.json()



napi = nekos_api = NekosAsyncAPI("https://nekos.life/api/v2")