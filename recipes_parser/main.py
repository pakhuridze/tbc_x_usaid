import asyncio
import time
import aiohttp
from scraper import fetch_page, fetch_full_recipe
from data_fetching import (collection , get_average_recipe_count,get_author_with_most_recipes,
                           get_recipe_with_most_portion,get_average_steps_to_cook)

async def full_recipes(session, recipes):
    tasks = [asyncio.create_task(fetch_full_recipe(session, recipe['recipe_link'])) for recipe in recipes]
    full_recipe_details = await asyncio.gather(*tasks)

    for recipe, full_details in zip(recipes, full_recipe_details):
        if full_details:
            recipe['ingredients'] = full_details['ingredients']
            recipe['steps'] = full_details['steps']
            recipe['portion_count'] = int(full_details['portion'])
            recipe['subcategory_link'] = full_details['subcategory_link']
        else:
            recipe['ingredients'] = 'Ingredients not found'
            recipe['steps'] = 'Steps not found'
            recipe['portion_count'] = 0
            recipe['subcategory_link'] = 'Subcategory link not found'

    if recipes and collection.count_documents({})==0:
        collection.insert_many(recipes)

async def main():
    async with aiohttp.ClientSession() as session:
       
        page_tasks = [asyncio.create_task(fetch_page(session, page)) for page in range(1, 4)]
        page_results = await asyncio.gather(*page_tasks)

        all_recipes = [recipe for page_recipes in page_results for recipe in page_recipes]

        await full_recipes(session, all_recipes)
      
        if collection.count_documents({})!=0:
              average_ingredients = get_average_recipe_count()
              print(f"Average number of ingredients per recipe: {average_ingredients}")
  
              average_steps = get_average_steps_to_cook()
              print(f"Average number of steps per recipe: {average_steps}")
  
              recipe_most_portions = get_recipe_with_most_portion()
              print(f"Recipe with the most portions: {recipe_most_portions['title']} - {recipe_most_portions['recipe_link']}")
  
              author_most_recipes = get_author_with_most_recipes()
              print(f"Author with the most recipes: {author_most_recipes}")

if __name__ == "__main__":
    start_time = time.perf_counter()
    asyncio.run(main())
    elapsed_time = time.perf_counter() - start_time
    print(f"Elapsed time: {elapsed_time:.2f} seconds")
