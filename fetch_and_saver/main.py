import asyncio
import aiohttp
import time
import json
import aiofiles


async def fetch_data(session, url):
    async with session.get(url) as response:
        return await response.json()


async def main():
    start_time = time.time()
    lock = asyncio.Lock()  # Create the lock

    async with aiohttp.ClientSession() as session:
        tasks = [
            fetch_data(session, f"https://jsonplaceholder.typicode.com/posts/{post_id}")
            for post_id in range(1, 71)
        ]
        # Await all tasks
        results = await asyncio.gather(*tasks)

        # Write the results to a JSON file with the lock
        async with lock:  # Lock used here as per your request
            async with aiofiles.open("posts.json", "w") as f:
                await f.write(json.dumps(results, indent=3))

    print(f"Time taken: {time.time() - start_time} seconds")


if __name__ == "__main__":
    asyncio.run(main())
