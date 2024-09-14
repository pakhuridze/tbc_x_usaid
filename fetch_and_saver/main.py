import asyncio
import aiohttp
import json
import time

start_time = time.time()

async def fetch_and_save(post_id, lock_thread, file):
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                async with lock_thread:
                    json.dump(data, file, indent=1)
                    file.write(',\n')  # Ensure each JSON object is on a new line
            else:
                print(f"Can't fetch data for post ID {post_id}")


async def main():
    lock = asyncio.Lock()

    # Open file once and pass it to fetch_and_save tasks
    with open("posts.json", "w") as file:
        file.write('[')  # Start the JSON array

        tasks = []
        for i in range(1, 78):
            tasks.append(fetch_and_save(i, lock, file))

        await asyncio.gather(*tasks)

        file.seek(0, 2)  # Move to the end of the file
        file.seek(file.tell() - 2, 0)  # Move back to overwrite the last comma
        file.write(']')  # End the JSON array

if __name__ == "__main__":
    asyncio.run(main())

end_time = time.time()

print(f"Start Time: {start_time}")
print(f"End Time: {end_time}")
print(f"Total Time Taken: {end_time - start_time} seconds")
