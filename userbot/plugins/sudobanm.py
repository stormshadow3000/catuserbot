#fake
from telethon import events
import asyncio
import os
import sys
import random
from userbot.utils import edit_or_reply
from . import *


@catub.cat_cmd(pattern=r"sudogban$")
async def _(event):
    reply_message = await event.get_reply_message()
    username = reply_message.sender.first_name
    if event.fwd_from:
        return
    await event.edit("gbanning This basterd.... \nfrom all over the world")
    await asyncio.sleep(6)
    h=(random.randrange(1,4))
    if h==1:
        
        k = await event.get_reply_message()
        username = k.sender.first_name
        await event.edit(f"Gbanning {username} from all sudo u have \nchat affected:- 24763")
        await asyncio.sleep(3)
        await event.edit(f"Gbanning {username} from all sudo u have \nchat affected:- 33577")
        await asyncio.sleep(3)
        await event.edit(f"Gbanning {username} from all sudo u have \nchat affected:- 49357")
        await asyncio.sleep(3)
        await event.edit(f"Gbanned {username} from all sudo u have \nchat affected:- 51320")
    if h==2:
        await event.edit(f"Gbanning {username} from all sudo u have \nchat affected:- 25799")
        await asyncio.sleep(3)
        await event.edit(f"Gbanning {username} from all sudo u have \nchat affected:- 36379")
        await asyncio.sleep(3)
        await event.edit(f"Gbanning {username} from all sudo u have \nchat affected:- 48993")
        await asyncio.sleep(3)
        await event.edit(f"Gbanned {username} from all sudo u have \nchat affected:- 51362")
    if h==3:
        await event.edit(f"Gbanning {username} from all sudo u have \nchat affected:- 24763")
        await asyncio.sleep(3)
        await event.edit(f"Gbanning {username} from all sudo u have \nchat affected:- 37362")
        await asyncio.sleep(3)
        await event.edit(f"Gbanning {username} from all sudo u have \nchat affected:- 46792")
        await asyncio.sleep(3)
        await event.edit(f"Gbanned {username} from all sudo u have \nchat affected:- 51332")
