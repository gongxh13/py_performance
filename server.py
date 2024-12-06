import asyncio
import websockets

async def handler(websocket, path):
    async for message in websocket:
        print(f"Received message from client: {message}")

async def main():
    async with websockets.serve(handler, "localhost", 8765):
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())
