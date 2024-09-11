import threading
import json
import requests
import time

start_time = time.time()

posts_arr = []
lock = threading.Lock()


def fetch_and_save(post_id):
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        with lock:
            posts_arr.append(data)
    else:
        print("Can't fetch data")


threads = []

for i in range(1, 78):
    thread = threading.Thread(target=fetch_and_save, args=(i,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

# sort data after fetching
posts_arr.sort(key=lambda x: x["id"])

# add sorted json
with open("posts.json", "w") as f:
    json.dump(posts_arr, f, indent=3)

end_time = time.time()

print(f"Start Time: {start_time}")
print(f"End Time: {end_time}")
print(f"Total Time Taken: {end_time - start_time} seconds")
