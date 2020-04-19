import aiohttp
import asyncio
from json import dumps
from os import getenv
from dotenv import load_dotenv
load_dotenv('.env')

class Error(Exception):
    pass

class ParameterError(Error):
    def __init__(self, expresion:str, mensaje:str):
        self.expresion = expresion
        self.mensaje = mensaje

APIKEY = getenv("APIKEY", "")
METHODS = ["get", "patch", "put", "post", "delete"]
API_URL = "https://otherworld-api.herokuapp.com" 

def gen_uri(endpoint:str):
    if endpoint is None:
        raise ParameterError("Invalid endpoint", f"{endpoint} is None")

    if endpoint.startswith("/"): endpoint = endpoint[1:]
    if endpoint.endswith("/"): endpoint = endpoint[:-1] 

    return f"{API_URL}/{endpoint}"

async def request(method:str, endpoint:str, body:dict={}):
    if method is None or method.lower() not in METHODS:
        raise ParameterError("Invalid method", f"{method} is an invalid method")
    
    if endpoint is None:
        raise ParameterError("Invalid endpoint", f"{endpoint} is None")
    
    uri = gen_uri(endpoint)
    body = dumps(body)
    
    headers = {
        'authorization': APIKEY,
        'content-type': "application/json"
    }

    async with aiohttp.ClientSession() as session:
        async with session.request(method, uri, data=body, headers=headers) as res:
            data = await res.json()
            data.status_code = res.status
            return data
