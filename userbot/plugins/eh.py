import random

from userbot import catub

from ..core.managers import edit_or_reply
from . import catmemes

plugin_category = "fun"
NO = [
 "( ͡° ͜ʖ ͡°)", "(ʘ‿ʘ)", "(✿´‿`)", "=͟͟͞͞٩(๑☉ᴗ☉)੭ु⁾⁾",
         "°˖✧◝(⁰▿⁰)◜✧˖°", "✌(-‿-)✌", "⌒°(❛ᴗ❛)°⌒", "(ﾟ<|＼(･ω･)／|>ﾟ)", "ヾ(o✪‿✪o)ｼ",
]

@catub.cat_cmd(
    pattern="eh$",
    command=("n", plugin_category),
    info={
        "header": " eh the people..",
        "usage": "{tr}eh",
    },
)
async def _(e):
    "yes the people."
    txt = random.choice(NO)
    await edit_or_reply(e, txt)
