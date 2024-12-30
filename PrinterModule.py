"""
███████████████████████████████████████████████████████████████████
██▄─▄█─▄▄▄▄█─█─██▀▄─██▄─█─▄██▄─▀█▀─▄█─▄▄─█▄─▄▄▀█▄─██─▄█▄─▄███▄─▄▄─█
███─██▄▄▄▄─█─▄─██─▀─███─▄▀████─█▄█─██─██─██─██─██─██─███─██▀██─▄█▀█
▀▀▄▄▄▀▄▄▄▄▄▀▄▀▄▀▄▄▀▄▄▀▄▄▀▄▄▀▀▄▄▄▀▄▄▄▀▄▄▄▄▀▄▄▄▄▀▀▀▄▄▄▄▀▀▄▄▄▄▄▀▄▄▄▄▄▀
©Copyright 2024 t.me/Name_Usernames4
This program is free software; you can redistribute it and/or modify
"""
#meta developer: @Name_Surnames4
__version__ = (0, 1, 5)
#name: Printer

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
    """Модуль для отправки сообщений / нажатий на кнопку 
    на втором аккаунте с основного"""
    strings = {"name": "Printer"}
    @loader.command()
    async def prt(self, message):
        """ {text} Написать {text} в ответном сообщении со второго
        аккаунта"""
        args = utils.get_args_raw(message)
        try:
            args = str(args)
            await message.reply(args)
            await message.delete()
        except Exception as e:
            await message.edit(f"Произошла ошибка: {e}")    
    @loader.command()
    async def clk(self, message):
        """ {reply} {button id} Нажать на кнопку в сообщении,
        на которое вы ответили (айди кнопки начинается с 0)"""
        args = utils.get_args_raw(message)
        try:
            args = int(args)
            await r.click(args)
            await message.delete()
        except Exception as e:
            await message.edit(f"Ошибка: {e}")
        
