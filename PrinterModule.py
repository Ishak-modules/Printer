"""
█████████████████
█─▄─▄─█─█─█▄─▄▄─█
███─███─▄─██─▄█▀█
▀▀▄▄▄▀▀▄▀▄▀▄▄▄▄▄▀
███████████████████████████████████████
█▄─▀█▀─▄█─▄▄─█▄─▄▄▀█▄─██─▄█▄─▄███▄─▄▄─█
██─█▄█─██─██─██─██─██─██─███─██▀██─▄█▀█
▀▄▄▄▀▄▄▄▀▄▄▄▄▀▄▄▄▄▀▀▀▄▄▄▄▀▀▄▄▄▄▄▀▄▄▄▄▄▀
███████████████████████
█▄─█▀▀▀█─▄██▀▄─██─▄▄▄▄█
██─█─█─█─███─▀─██▄▄▄▄─█
▀▀▄▄▄▀▄▄▄▀▀▄▄▀▄▄▀▄▄▄▄▄▀
███████████████████████████████████████████
█─▄▄▄─█▄─▄▄▀█▄─▄▄─██▀▄─██─▄─▄─█▄─▄▄─█▄─▄▄▀█
█─███▀██─▄─▄██─▄█▀██─▀─████─████─▄█▀██─██─█
▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀▀▄▄▄▀▀▄▄▄▄▄▀▄▄▄▄▀▀
█████████████
█▄─▄─▀█▄─█─▄█
██─▄─▀██▄─▄██
▀▄▄▄▄▀▀▀▄▄▄▀▀
███████████████████████████
█▄─▄█─▄▄▄▄█─█─██▀▄─██▄─█─▄█
██─██▄▄▄▄─█─▄─██─▀─███─▄▀██
▀▄▄▄▀▄▄▄▄▄▀▄▀▄▀▄▄▀▄▄▀▄▄▀▄▄▀
©Copyright 2024 t.me/Name_Usernames4
This program is free software; you can redistribute it and/or modify
"""
#name: Printer
#meta developer: @Name_Surnames4
__version__ = (0, 1, 5)

import asyncio
import time
from telethon.tl.types import Message, ChatAdminRights
from telethon import events, functions, types
import logging
import re
from .. import loader, utils
from asyncio import sleep
import random
logger = logging.getLogger(__name__)
import hikkatl
from hikkatl.errors.rpcerrorlist import FloodWaitError
import inspect
# сам класс модуля
@loader.tds
class printer(loader.Module):
    strings = {"name": "Printer"}
    @loader.command()
    async def prt(self, message):
        args = utils.get_args_raw(message)
        try:
            args = str(args)
            await message.reply(args)
            await message.delete()
        except Exception as e:
            await message.edit(f"Произошла ошибка: {e}")    
    @loader.command()
    async def clk(self, message):
        args = utils.get_args_raw(message)
        try:
            args = int(args)
            await r.click(args)
            await message.delete()
        except Exception as e:
            await message.edit(f"Ошибка: {e}")
        
