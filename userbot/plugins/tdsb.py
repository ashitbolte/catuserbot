import requests
from validators.url import url
from userbot import catub
from ..core.managers import edit_delete, edit_or_reply
plugin_category = "Extra"

@catub.cat_cmd(
    pattern="tdsb(?: |$)(.*)",
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
    await edit_or_reply(event, f"Read [bootloopfix from here](https://telegra.ph/How-to-delete-a-Magisk-module-from-Recovery-06-06) Before Flashing Anything.\n\n》 Then Download and Flash **{device}** Dsb from This Link : [Click here]({pling})\n\n》 Report here if it's either working as expected or not on your Device 👍")
    
# Thanks to jisan 🤩
