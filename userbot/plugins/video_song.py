# Plugin made by @hellboi_atul for DARK COBRA..
# You can use this..but don't edit/remove these comment lines..
# This module fetches the link from YouTube for the given query..
# merged .uta
# So wahi...Enjoy


import re
import random

import asyncio
import os
from pathlib import Path
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot import catub

from ..core.managers import edit_or_reply


plugin_category = "songs"

IF_EMOJI = re.compile(
    "["
    "\U0001F1E0-\U0001F1FF"  # flags (iOS)
    "\U0001F300-\U0001F5FF"  # symbols & pictographs
    "\U0001F600-\U0001F64F"  # emoticons
    "\U0001F680-\U0001F6FF"  # transport & map symbols
    "\U0001F700-\U0001F77F"  # alchemical symbols
    "\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
    "\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
    "\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
    "\U0001FA00-\U0001FA6F"  # Chess Symbols
    "\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
    "\U00002702-\U000027B0"  # Dingbats 
    "]+")

def deEmojify(inputString: str) -> str:
    """Remove emojis and other non-safe characters from string"""
    return re.sub(IF_EMOJI, '', inputString)


@catub.cat_cmd(pattern="yv ?(.*)")

async def nope(doit):
    ok = doit.pattern_match.group(1)
    if not ok:
        if doit.is_reply:
            what = (await doit.get_reply_message()).message
        else:
            await doit.edit("`Please give some query to search..!`")
            return
    sticcers = await bot.inline_query(
        "vid", f"{(deEmojify(ok))}")
    await sticcers[0].click(doit.chat_id,
                            reply_to=doit.reply_to_msg_id,
                            silent=True if doit.is_reply else False,
                            hide_via=True)
    await doit.delete()






# Social Distancing..







@catub.cat_cmd(pattern="ys ?(.*)")

async def nope(doit):
    ok = doit.pattern_match.group(1)
    if not ok:
        if doit.is_reply:
            what = (await doit.get_reply_message()).message
        else:
            await doit.edit("`Sir please give some query to search and download it for you..!`")
            return
    sticcers = await bot.inline_query(
        "Lybot", f"{(deEmojify(ok))}")
    await sticcers[0].click(doit.chat_id,
                            reply_to=doit.reply_to_msg_id,
                            silent=True if doit.is_reply else False,
                            hide_via=True)
    await doit.delete()



SEARCH_STRING = "<code>Ok weit, searching....</code>"
NOT_FOUND_STRING = "<code>Sorry !I am unable to find any results to your query</code>"
SENDING_STRING = "<code>Ok I found something related to that.....</code>"
BOT_BLOCKED_STRING = "<code>Please unblock @utubebot and try again</code>"

 