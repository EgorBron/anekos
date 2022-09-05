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

from . import httpai, errors
import urllib, aiohttp

noresponse = "Couldn't contact the API right now..."

_possible_everywhere = ['tickle', 'spank', 'neko', 'waifu', 'baka', 'ngif', 'cuddle', 'avatar', 'holo', 'kiss', 'fox_girl', 'poke', 'goose', 'pat', 'slap', 'woof', 'wallpaper', 'hug', 'smug', 'gecg', 'gasm', 'lizard', 'feed', '8ball']
_possible_nsfw = [
    'feet', 'yuri', 'trap', 'futanari', 'hololewd', 'lewdkemo',
    'solog', 'feetg', 'cum', 'erokemo', 'les', 'lewdk', 'eroyuri', 'eron',
    'cum_jpg', 'bj', 'nsfw_neko_gif', 'solo', 'kemonomimi', 'nsfw_avatar',
    'anal', 'hentai', 'erofeet',
    'keta', 'blowjob', 'pussy', 'tits', 'holoero', 'pussy_jpg',
    'pwankg', 'classic', 'kuni', 'femdom',
    'erok', 'boobs', 'random_hentai_gif',
    'smallboobs', 'ero'
]

async def eightball() -> dict:
    """That's 8ball!

    Raises:
        errors.NothingFound: API didn't return anything

    Returns:
        dict: Answer of 8ball
    """
    try:
        r = await httpai.nekos_api.get_as_json("/8ball")
        return {"text": r["response"], "image": r["url"]}
    except (KeyError, ValueError, aiohttp.client_exceptions.ClientConnectorError) as e:
        raise errors.NothingFound from e

async def img(target: str = None) -> str:
    """Gets random image from Nekos API by given category

    Args:
        target (str): Category of image

    Raises:
        errors.EmptyArgument: Category is None or not provided
        errors.InvalidArgument: Category is not in possible categories

    Returns:
        str: Link to the image
    """
    if target is None:
        raise errors.EmptyArgument(
            f"\nArguments SFW: {_possible_everywhere}\nArguments NSFW: {_possible_nsfw}"
        )
    
    target = target.lower()

    # line below is equals to two checks "target not in list"
    if target not in ((L:=list(_possible_everywhere)).extend(_possible_nsfw) or L):
        raise errors.InvalidArgument(
            f"You haven't added any valid arguments.\nArguments SFW: {_possible_everywhere}\nArguments NSFW: {_possible_nsfw}"
        )

    try:
        target = target.replace("random_hentai_gif", "Random_hentai_gif")
        r = await httpai.nekos_api.get_as_json("/img/" + target)
        return r["url"]
    except (KeyError, ValueError, aiohttp.client_exceptions.ClientConnectorError) as e:
        raise errors.NothingFound from e


async def owoify(text: str = None) -> str:
    """OwOifies inputted text
    
    wau this is so usefuw anyd coow

    Args:
        text (str): Text to OwOify

    Raises:
        errors.NothingFound: API didn't return anything
        errors.EmptyArgument: Text is None or not provided

    Returns:
        str: OwOified text
    """
    if text is None:
        raise errors.EmptyArgument

    try:
        r = await httpai.nekos_api.get_as_json("/owoify?text=" + urllib.parse.quote(text))
        return r["owo"]
    except (KeyError, ValueError, aiohttp.client_exceptions.ClientConnectorError) as e:
        raise errors.NothingFound from e


async def spoiler(text: str = None) -> str:
    """Marks every character in inputted text as spoler

    Args:
        text (str): Text to make it "spoilered"

    Raises:
        errors.NothingFound: API didn't return anything
        errors.EmptyArgument: Text is None or not provided

    Returns:
        str: ||S||||p||||o||||i||||l||||e||||r||||s||
    """
    if text is None:
        raise errors.EmptyArgument
    try:
        r = await httpai.nekos_api.get_as_json("/spoiler?text=" + urllib.parse.quote(text))
        return r["owo"]
    except (KeyError, ValueError, aiohttp.client_exceptions.ClientConnectorError) as e:
        raise errors.NothingFound from e


async def cat() -> str:
    """Random cat picture

    Raises:
        errors.NothingFound: API didn't return anything

    Returns:
        str: Link to random cat image
    """
    try:
        return (await httpai.nekos_api.get_as_json("/img/meow"))["url"]
    except (KeyError, ValueError, aiohttp.client_exceptions.ClientConnectorError) as e:
        raise errors.NothingFound from e


async def textcat() -> str:
    """Random text cat

    Raises:
        errors.NothingFound: API didn't return anything

    Returns:
        str: Cool cat made using symbols
    """
    try:
        return (await httpai.nekos_api.get_as_json("/cat"))["cat"]
    except (KeyError, ValueError, aiohttp.client_exceptions.ClientConnectorError) as e:
        raise errors.NothingFound from e

async def why() -> str:
    """Random "why" question

    Raises:
        errors.NothingFound: API didn't return anything

    Returns:
        str: Random "why" question (yeah)
    """
    try:
        return (await httpai.nekos_api.get_as_json("/why"))["why"]
    except (KeyError, ValueError, aiohttp.client_exceptions.ClientConnectorError) as e:
        raise errors.NothingFound from e


async def fact() -> str:
    """Random fact

    Raises:
        errors.NothingFound: API didn't return anything

    Returns:
        str: Random fact!
    """
    try:
        return (await httpai.nekos_api.get_as_json("/fact"))["fact"]
    except (KeyError, ValueError, aiohttp.client_exceptions.ClientConnectorError) as e:
        raise errors.NothingFound from e


async def name() -> str:
    """Generates (?) random name

    Raises:
        errors.NothingFound: API didn't return anything

    Returns:
        str: Generated name
    """
    try:
        return (await httpai.nekos_api.get_as_json("/name"))["name"]
    except (KeyError, ValueError, aiohttp.client_exceptions.ClientConnectorError) as e:
        raise errors.NothingFound from e