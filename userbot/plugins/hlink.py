import requests
from validators.url import url
from userbot import catub
from ..core.managers import edit_delete, edit_or_reply
plugin_category = "Extra"

@catub.cat_cmd(
    pattern="hlink(?: |$)(.*)",
    command=("tdsb", plugin_category),
    info={
        "header": "Asks User To Try DSB from given Pling Link.",
        "usage": "{tr}tdsb <url> <DSB-File-name>",   
    },
)
async def _(event):
    "Ask User To Try DSB from given Pling Link."
    reply_to = await reply_id(event)
    inpt = event.pattern_match.group((1))
    pling = None
    if " " in inpt:
        pling, device = inpt.split(" ", (1))
    if not inpt or not pling:
        return await edit_delete(event, "`Give an input`")
    if not pling.startswith("https://"):
        return await edit_delete(event, "`the given pling link is not correct`")
    await edit_or_reply(event, f"[{device}]({pling})")
    
# Thanks to jisan 🤩
