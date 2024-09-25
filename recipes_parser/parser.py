BASE_URL = "https://kulinaria.ge"


def parse_recipes(soup):
    find_parent_div = soup.find('div', class_='kulinaria-row box-container')
    find_recipe_div = find_parent_div.find_all('div', class_='box box--author kulinaria-col-3 box--massonry')

    recipes = []

    for recipe in find_recipe_div:
        recipe_anchor = recipe.find('a', class_='box__title')
        recipe_title = recipe_anchor.get_text(strip=True)
        recipe_link = recipe_anchor.get('href')
        full_link = f"{BASE_URL}{recipe_link}" if recipe_link else 'Recipe link not found'

        recipe_description = recipe.find('div', class_='box__desc').get_text(strip=True) if recipe.find('div',
                                                                                                        class_='box__desc') else 'Description not found'

        image_tag = recipe.find('div', class_='box__img').find('img') if recipe.find('div', class_='box__img') else None
        image_link = f"{BASE_URL}{image_tag.get('src')}" if image_tag else 'Image not found'

        author_name = recipe.find('div', class_='box__author').find('a').get_text(strip=True) if recipe.find('div',
                                                                                                             class_='box__author') else 'Unknown'
        active_star_count = len(
            [star for star in recipe.find_all('div', class_='post-star__item') if 'act' in star['class']])

        recipes.append({
            'title': recipe_title,
            'description': recipe_description,
            'recipe_link': full_link,
            'image': image_link,
            'author': author_name,
            'rating': active_star_count
        })


    return recipes
