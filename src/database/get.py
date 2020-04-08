from database.utils import request 
import asyncio
loop = asyncio.get_event_loop()

async def player(id:str):
    res = await request("get", f"/game/player", { "playerid": f"{id}"})
    return res
