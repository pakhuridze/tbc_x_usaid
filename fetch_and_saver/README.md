# Async JSON Fetcher

This project fetches JSON data from a public API and saves it to a file asynchronously using Python's `asyncio` and `aiohttp` libraries.

## Description

The script fetches posts from the JSONPlaceholder API and writes them to a `posts.json` file. It uses asynchronous programming to handle multiple requests concurrently, improving performance.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/async-json-fetcher.git
    cd async-json-fetcher
    ```

2. Create a virtual environment and activate it:
    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

Run the script:
```sh
python main.py

The script will fetch posts from the API and save them to posts.json.

Requirements

Python 3.7+
aiohttp
asyncio