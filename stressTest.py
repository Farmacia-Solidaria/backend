import aiohttp
import time
import asyncio

def avg(list):
    return sum(list)/len(list)

async def test(session):
    payload = {
        "username": "for error",
        "password": "for error"
    }
    start_time = time.time()
    async with session.post("http://localhost:8000/api/login/auth", data=payload) as res:
        data = await res.json()
        return time.time() - start_time


async def main():

    start_time = time.time()
    actions = []
    times = []
    
    async with aiohttp.ClientSession() as session:
        for i in range(1000):
            actions.append(asyncio.ensure_future(test(session)))
        
        times = await asyncio.gather(*actions)
    print(times)

    print("\n\n\nTotal time=", time.time() - start_time)
    print("Avg = ", avg(times))
    print("Max = ", max(times))
    print("Min = ", min(times))


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())