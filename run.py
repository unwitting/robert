import asyncio
from src import robert

async def hi():
    rob = robert.Robert()
    await rob.boot()

if __name__ == "__main__":
    asyncio.run(hi())
