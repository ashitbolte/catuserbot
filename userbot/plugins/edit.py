import asyncio

from telethon.events import NewMessage as NewMsg
from userbot import catub



@catub.cat_cmd(
    pattern="edit",
)
async def editer(edit):
    message = edit.text
    chat = await edit.get_input_chat()
    string = str(message[6:])
    reply = await edit.get_reply_message()
    if reply and reply.text:
        try:
            await reply.edit(string)
            await edit.delete()
        except BaseException:
            pass
    else:
        i = 1
        async for message in ultroid_bot.iter_messages(chat, ultroid_bot.uid):
            if i == 2:
                await message.edit(string)
                await edit.delete()
                break
            i = i + 1
