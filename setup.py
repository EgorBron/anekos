import re
from setuptools import setup

version = ""
with open("nekos/__init__.py") as f:
    version = re.search(
        r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE
    ).group(1)

if not version:
    raise RuntimeError("version is not set")

setup(
    name="anekos",
    author="EgorBron",
    url="https://github.com/EgorBron/anekos",
    version=version,
    packages=["anekos"],
    license="MIT",
    description="Async Nekos.life API interactor (just a shitty ver. of original module)",
    include_package_data=True,
    install_requires=["aiohttp", "ujson"],
)