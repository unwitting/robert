import asyncio
from src import robert
from src import server

async def hi():
    rob = robert.Robert()
    await rob.boot()
    server.start(rob)

if __name__ == "__main__":
    asyncio.run(hi())
