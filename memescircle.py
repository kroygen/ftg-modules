from telethon import functions, types, events
from .. import loader, utils
from telethon.errors.rpcerrorlist import YouBlockedUserError
import datetime
import random
from asyncio import sleep
def register(cb):
    cb(vibecircleMod())
class vibecircleMod(loader.Module):
    """Рандомные мемы из @vibe_circle"""
    strings = {'name': 'Круг'}
    def __init__(self):
        self.name = self.strings['name']
        self._me = None
        self._ratelimit = []
    async def client_ready(self, client, db):
        self._db = db
        self._client = client
        self.me = await client.get_me()
    async def krugcmd(self, message):
        """
        Рандомные мемы из @vibe_circle
        """
        await message.edit("<b>ПУK!!!</b>")
        chat = '@vibe_circle'
        result = await message.client(functions.messages.GetHistoryRequest(
        peer=chat,
        offset_id=0,
        offset_date=datetime.datetime.now(),
        add_offset=random.choice([1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,41,43,45,47,49,51,53,55,57,59,61,63,65,67,69,71,73,75,77,79,81,83,85,87,89,91,93,95,97,99,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120]),
        limit=1,
        max_id=0,
        min_id=0,
        hash=0
        ))
        await message.delete()
        await message.client.send_file(message.to_id, result.messages[0].media)

    async def krugokcmd(self, message):
        """
        Рандомные мемы из @repomem 
        """
        await message.edit("<b>Лови</b>")
        chat = '@memsheroes'
        result = await message.client(functions.messages.GetHistoryRequest(
        peer=chat,
        offset_id=0,
        offset_date=datetime.datetime.now(),
        add_offset=random.choice([1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,41,43,45,47,49,51,53,55,57,59,61,63,65,67,69,71,73,75,77,79,81,83,85,87,89,91,93,95,97,99,101]),
        limit=1,
        max_id=0,
        min_id=0,
        hash=0
        ))
        await message.delete()
        await message.client.send_file(message.to_id, result.messages[0].media)
    
            
