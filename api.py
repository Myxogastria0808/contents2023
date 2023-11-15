from fastapi import FastAPI
import json
from pathlib import Path
from fastapi.responses import FileResponse
from typing import Optional


app: FastAPI = FastAPI()

#/
@app.get("/")
async def index():
    current: Path = Path()
    file_path: Path = current /"data.json"
    return FileResponse(path=file_path)

#/detail?id=int
@app.get("/detail")
async def detail(id: int = 2):
    with open('./data.json', 'r') as f:
        json_load = json.load(f)
    return json_load['data'][id-1]

#/nyoki
@app.get("/nyoki")
async def halloween():
    return {'にょき': '·*·:≡( ε:)'}
