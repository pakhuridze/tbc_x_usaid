import aiohttp
from bs4 import BeautifulSoup

from parser import parse_recipes

BASE_URL = "https://kulinaria.ge"
HEADERS = {'User-Agent': 'Mozilla/5.0'}


async def fetch_page(session, page):
    url = f"{BASE_URL}/receptebi/cat/desertebi-da-tkbileuloba/?page={page}"
    try:
        async with session.get(url, headers=HEADERS) as response:
            if response.status == 200:
                html_content = await response.text()
                soup = BeautifulSoup(html_content, 'html.parser')
                return parse_recipes(soup)  # Use the external parser to extract basic recipe details
            else:
                print(f"Failed to retrieve page {page}: Status {response.status}")
                return []
    except aiohttp.ClientError as e:
        print(f"Client error while fetching page {page}: {e}")
        return []


async def fetch_full_recipe(session, recipe_link):
    try:
        async with session.get(recipe_link, headers=HEADERS) as response:
            if response.status == 200:
                html_content = await response.text()
                soup = BeautifulSoup(html_content, 'html.parser')

                # Extract ingredients
                ingredients_list = []
                ingredients_div = soup.find('div', class_='list')
                if ingredients_div:
                    ingredient_items = ingredients_div.find_all('div', class_='list__item')
                    for item in ingredient_items:
                        parts = item.get_text(strip=True).split()
                        quantity = parts[0] if len(parts) > 0 else ''
                        unit = parts[1] if len(parts) > 1 else ''
                        ingredient_name = ' '.join(parts[2:])
                        ingredients_list.append(f"{quantity} {unit} {ingredient_name}".strip())

                # Extract steps
                steps_list = []
                steps_div = soup.find('div', class_='lineList')
                if steps_div:
                    step_items = steps_div.find_all('div', class_='lineList__item')
                    for item in step_items:
                        step_number = item.find('div', class_='count').get_text(strip=True)
                        step_description = item.find('p').get_text(strip=True)
                        steps_list.append((int(step_number), step_description))

                steps = steps_list if steps_list else 'Steps not found'

                # Extract portion (ულუფა) data
                portion = 0
                lineDesc = soup.find('div', class_='lineDesc')
                if lineDesc:
                    for item in lineDesc.find_all('div', class_='lineDesc__item'):
                        text = item.get_text(strip=True)
                        if 'ულუფა' in text:
                            parts = text.split()
                            for part in parts:
                                if part.isdigit():
                                    portion = part
                                    break
                            if portion != 0:
                                break

                # Extract subcategory link
                subcategory_link = ''
                pagination_container = soup.find('div', class_='pagination-container')
                if pagination_container:
                    subcategory_tag = pagination_container.find_all('a')[
                        -1]
                    subcategory_link = BASE_URL + subcategory_tag['href'] if subcategory_tag else ''

                return {
                    'ingredients': ingredients_list,
                    'steps': steps,
                    'portion': portion,
                    'subcategory_link': subcategory_link
                }
            else:
                print(f"Failed to retrieve recipe at {recipe_link}: Status {response.status}")
                return None
    except aiohttp.ClientError as e:
        print(f"Client error while fetching recipe {recipe_link}: {e}")
        return None
