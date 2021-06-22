import random

from userbot import catub

from ..core.managers import edit_or_reply
from . import catmemes

plugin_category = "fun"
NO = [
 "(＠´＿｀＠)", "⊙︿⊙", "(▰˘︹˘▰)", "●︿●", "(　´_ﾉ` )", "彡(-_-;)彡",

]

@catub.cat_cmd(
    pattern="es$",
    command=("n", plugin_category),
    info={
        "header": " es the people..",
        "usage": "{tr}es",
    },
)
async def _(e):
    "yes the people."
    txt = random.choice(NO)
    await edit_or_reply(e, txt)
