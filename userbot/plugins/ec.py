import random

from userbot import catub

from ..core.managers import edit_or_reply


plugin_category = "fun"
NO = [
  "أ‿أ", "╥﹏╥", "(;﹏;)", "(ToT)", "(┳Д┳)", "(ಥ﹏ಥ)", "（；へ：）", "(T＿T)", "（πーπ）", "(Ｔ▽Ｔ)",
    "(⋟﹏⋞)", "（ｉДｉ）", "(´Д⊂ヽ", "(;Д;)", "（>﹏<）", "(TдT)", "(つ﹏⊂)", "༼☯﹏☯༽", "(ノ﹏ヽ)",
    "(ノAヽ)", "(╥_╥)", "(T⌓T)", "(༎ຶ⌑༎ຶ)", "(☍﹏⁰)｡", "(ಥ_ʖಥ)", "(つд⊂)", "(≖͞_≖̥)", "(இ﹏இ`｡)",
    "༼ಢ_ಢ༽", "༼ ༎ຶ ෴ ༎ຶ༽",

]

@catub.cat_cmd(
    pattern="ec$",
    command=("n", plugin_category),
    info={
        "header": " ec the people..",
        "usage": "{tr}ec",
    },
)
async def _(e):
    "yec the people."
    txt = random.choice(NO)
    await edit_or_reply(e, txt)
