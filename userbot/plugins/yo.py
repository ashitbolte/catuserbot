import asyncio

from userbot import catub

from ..core.managers import edit_or_reply

plugin_category = "fun"


@catub.cat_cmd(
    pattern="yo$",
    command=("oof", plugin_category),
    info={
        "header": "Animation command",
        "usage": "{tr}yo",
    },
)
async def Oof(e):
    "Animation command."
    t = "yo"
    catevent = await edit_or_reply(e, t)
    for _ in range(15):
        await asyncio.sleep(0.5)
        t = t[:-1] + "oo"
        await catevent.edit(t)
