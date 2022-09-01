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
import urllib

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

    Returns:
        dict: Answer of 8ball
    """
    r = await httpai.nekos_api.get_as_json("/8ball")
    return {"text": r["response"], "image": r["url"]}


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
            f"You have to at least define an argument in string format\nArguments SFW: {_possible_everywhere}\nArguments NSFW: {_possible_nsfw}"
        )

    if target.lower() not in _possible_everywhere or target.lower() not in _possible_nsfw:
        raise errors.InvalidArgument(
            f"You haven't added any valid arguments\nArguments SFW: {_possible_everywhere}\nArguments NSFW: {_possible_nsfw}"
        )

    #try:
    if target.lower() == "random_hentai_gif":
        r = await httpai.nekos_api.get("/img/Random_hentai_gif")
    else:
        r = await httpai.nekos_api.get("/img/" + target.lower())
    # that's very ugly
    #except Exception:
    #    raise errors.NothingFound(noresponse)

    return r["url"]


async def owoify(text: str = None) -> str:
    """OwOifies inputted text
    
    wau this is so usefuw anyd coow

    Args:
        text (str): Text to OwOify

    Raises:
        errors.EmptyArgument: Text is None or not provided

    Returns:
        str: OwOified text
    """
    if text is None:
        raise errors.EmptyArgument(
            "You have to enter a string you want to enter to API"
        )

    r = await httpai.nekos_api.get("/owoify?text=" + urllib.parse.quote(text))
    return r["owo"]


async def spoiler(text: str = None) -> str:
    """Marks every character in inputted text as spoler

    Args:
        text (str): Text to make it "spoilered"

    Raises:
        errors.EmptyArgument: Text is None or not provided

    Returns:
        str: ||S||||p||||o||||i||||l||||e||||r||||s||
    """
    if text is None:
        raise errors.EmptyArgument(
            "You have to enter a string you want to enter to API"
        )

    r = await httpai.nekos_api.get("/spoiler?text=" + urllib.parse.quote(text))
    return r["owo"]


async def cat() -> str:
    """Random cat picture

    Returns:
        str: Link to random cat image
    """
    #try:
    return (await httpai.nekos_api.get("/img/meow"))["url"]
    #except Exception:
    #    raise errors.NothingFound(noresponse)


async def textcat() -> str:
    """Random text cat

    Returns:
        str: Cool cat made using symbols
    """
    #try:
    return (await httpai.nekos_api.get("/cat"))["cat"]
    #except Exception:
    #    raise errors.NothingFound(noresponse)


async def why() -> str:
    """Random "why" question

    Returns:
        str: Random "why" question (yeah)
    """
    #try:
    return (await httpai.nekos_api.get("/why"))["why"]
    #except Exception:
    #    raise errors.NothingFound(noresponse)


async def fact() -> str:
    """Random fact

    Returns:
        str: Random fact!
    """
    #try:
    return (await httpai.nekos_api.get("/fact"))["fact"]
    #except Exception:
    #    raise errors.NothingFound(noresponse)


async def name() -> str:
    """Generates (?) random name

    Returns:
        str: Generated name
    """
    #try:
    return (await httpai.nekos_api.get("/name"))["name"]
    #except Exception:
    #    raise errors.NothingFound(noresponse)