import asyncio
import aiohttp
import time
import json


async def fetch_data(session, url):
    async with session.get(url) as response:
        return await response.json()


async def main():
    start_time = time.time()
    lock = asyncio.Lock()  # Create the lock
    async with aiohttp.ClientSession() as session:
        tasks = []
        for post_id in range(1, 78):
            url = f"https://jsonplaceholder.typicode.com/todos/{post_id}"
            tasks.append(fetch_data(session, url))

        # Await all tasks
        results = await asyncio.gather(*tasks)

        # Write the results to a JSON file with the lock
        async with lock:
            with open("posts.json", "w") as f:
                json.dump(results, f, indent=3)

    print(f"Time taken: {time.time() - start_time} seconds")


if __name__ == "__main__":
    asyncio.run(main())
