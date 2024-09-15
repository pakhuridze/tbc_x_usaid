import json
import threading
import time

import requests

start_time = time.time()


def fetch_and_save(post_id, lock_thread, file):
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        with lock_thread:
            # Lock for file operations to prevent race conditions
            file.write(json.dumps(data, indent=3))
            file.write(',\n')  # Ensure each JSON object is on a new line
    else:
        print(f"Can't fetch data for post ID {post_id}")


def main():
    lock = threading.Lock()

    with open("posts.json", "w") as file:
        file.write('[')  # Start the JSON array

        threads = []
        for i in range(1, 78):
            thread = threading.Thread(target=fetch_and_save, args=(i, lock, file))
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()

        # Go back to remove the last comma
        file.seek(file.tell() - 2, 0)  # Move back to overwrite the last comma
        file.write(']')  # End the JSON array


if __name__ == "__main__":
    main()

end_time = time.time()

print(f"Start Time: {start_time}")
print(f"End Time: {end_time}")
print(f"Total Time Taken: {end_time - start_time} seconds")
