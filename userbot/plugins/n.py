import random

from userbot import catub

from ..core.managers import edit_or_reply
from . import catmemes

plugin_category = "fun"
NO = [
 "`ᑎⓄ`",
 "`no no`",
 "𝓝ㄖ",
 "╭━┳╮\n┃┃┃┣━╮\n┃┃┃┃╋┃\n╰┻━┻━╯",
 "╔═╦╗\n║║║╠═╗\n║║║║╬║\n╚╩═╩═╝",
 "█▀▀▄ █▀▀█ \n█──█ █──█ \n▀──▀ ▀▀▀▀",
 "╔═╗─╔╗\n║║╚╗║║\n║╔╗╚╝╠══╗\n║║╚╗║║╔╗║\n║║─║║║╚╝║\n╚╝─╚═╩══╝",
 "██████████████\n█▄─▀█▄─▄█─▄▄─█\n██─█▄▀─██─██─█\n▀▄▄▄▀▀▄▄▀▄▄▄▄▀",
]

@catub.cat_cmd(
    pattern="n$",
    command=("n", plugin_category),
    info={
        "header": " no the people..",
        "usage": "{tr}n",
    },
)
async def _(e):
    "yes the people."
    txt = random.choice(NO)
    await edit_or_reply(e, txt)
