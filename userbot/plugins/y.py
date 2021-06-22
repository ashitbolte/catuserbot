import random

from userbot import catub

from ..core.managers import edit_or_reply
from . import catmemes

plugin_category = "fun"
YES = [
 "`yes yes`",
 "`yo!`",
 "Yོeོsོ",
 "【Y】【e】【s】",
 "『Y』『e』『s』",
 "────╔═╗\n╔╦╦═╣═╣\n║║║╩╬═║\n╠╗╠═╩═╝\n╚═╝",
 "╔╗─╔╦══╦══╗\n║║─║║║═╣══╣\n║╚═╝║║═╬══║\n╚═╗╔╩══╩══╝\n╔═╝║\n╚══╝",
 "╭╮╱╭┳━━┳━━╮\n┃┃╱┃┃┃━┫━━┫\n┃╰━╯┃┃━╋━━┃\n╰━╮╭┻━━┻━━╯\n╭━╯┃\n╰━━╯",
]

@catub.cat_cmd(
    pattern="y$",
    command=("y", plugin_category),
    info={
        "header": " yes the people..",
        "usage": "{tr}y",
    },
)
async def _(e):
    "yes the people."
    txt = random.choice(YES)
    await edit_or_reply(e, txt)
