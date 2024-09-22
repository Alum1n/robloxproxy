from roblox import Client
from fastapi import FastAPI

app = FastAPI()
client = Client("ROBLOSECURITYHERE")

universe_id = 13058

@app.get("/player-count")
async def get_player_count():
    universe = await client.get_universe(universe_id)
    return {
        "player_count": universe.playing
    }
