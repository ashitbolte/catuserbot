# Modded from dagd.py
"""
Animate How To Google
Command .htg Search Query
By @loxxi
"""

import requests
from validators.url import url

from userbot import catub

from ..core.managers import edit_delete, edit_or_reply

plugin_category = "utils"

@catub.cat_cmd(pattern="htg (.*)")
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    sample_url = "https://da.gd/s?url=https://lmgtfy.com/?q={}%26iie=1".format(
        input_str.replace(" ", "+")
    )
    response_api = requests.get(sample_url).text
    if response_api:
        await event.edit(
            "[{}]({})\n`Thank me Later 🙃` ".format(input_str, response_api.rstrip())
        )
    else:
        await event.edit("something is wrong. please try again later.")


 