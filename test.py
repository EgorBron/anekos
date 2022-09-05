import anekos, asyncio

async def a():
    print(await anekos.cat())
    print(await anekos.eightball())
    print(await anekos.owoify("so cool text is changed"))
    print(await anekos.fact())
    print(await anekos.img("wallpaper"))
    print(await anekos.spoiler("aaa"))
    print(await anekos.name())
    print(await anekos.textcat())
    print(await anekos.why())

asyncio.run(a())