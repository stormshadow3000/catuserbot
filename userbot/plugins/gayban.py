#fake
from telethon import events
import asyncio
import os
import sys
import random
from userbot.utils import edit_or_reply
from . import *


@catub.cat_cmd(pattern=r"gayban$")
async def _(event):
    reply_message = await event.get_reply_message()
    username = reply_message.sender.first_name
    if event.fwd_from:
        return
    await event.edit("gbanning This fumcker ass.... \nfrom telegram")
    await asyncio.sleep(3)
    h=(random.randrange(1,4))
    if h==1:
        
        k = await event.get_reply_message()
        username = k.sender.first_name
        await event.edit(f"Gbanning {username} from all sudo u have ")
        await asyncio.sleep(3)
        await event.edit(f"Gbanning  This gay {username} ")
        await asyncio.sleep(3)
        await event.edit(f"#Gbanned \n{username} \nfrom spam watch \nfrom chutiya watch \nfrom Randwa watch \nchats affected :- 43958 ")
     
    if h==2:
        await event.edit(f"Gbanning {username} from all sudo u have ")
        await asyncio.sleep(3)
        await event.edit(f"Gbanning  This gay {username} ")
        await asyncio.sleep(3)
        await event.edit(f"#Gbanned \n{username} \nfrom spam watch \nfrom chutiya watch \nfrom Randwa watch  \nchats affected :- 43958 ")
    if h==3:
        await event.edit(f"Gbanning {username} from all sudo u have ")
        await asyncio.sleep(3)
        await event.edit(f"Gbanning  This gay {username} ")
        await asyncio.sleep(3)
        await event.edit(f"#Gbanned \n{username} \nfrom spam watch \nfrom chutiya watch \nfrom Randwa watch  \nchats affected :- 43958 ")
