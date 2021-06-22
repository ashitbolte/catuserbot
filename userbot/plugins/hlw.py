import random

from userbot import catub

from ..core.managers import edit_or_reply


HIIREACTS = [
   "`hi`",
   "`hello`",
   " `hey, hello !! `",
   "`Hey buddy !!`",
   "`hello dude !!`",
   "`sup !?`",
   "`whats up boi !?`",
   "`hey sar !`",
   "`Howdy , howdy !!`",
   "`hey ! `",
]

plugin_category = "funpro"


@catub.cat_cmd(
    pattern="hlw$",
    command=("hlw"),
    info={
        "header": " hii the people..",
        "usage": "{tr}hii",
    },
)
async def _(e):
    "hii the people."
    txt = random.choice(HIIREACTS)
    await edit_or_reply(e, txt)

