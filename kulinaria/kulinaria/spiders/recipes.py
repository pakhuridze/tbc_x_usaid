import scrapy
import re

class RecipesSpider(scrapy.Spider):
    name = "recipes"
    allowed_domains = ["kulinaria.ge"]
    start_urls = ["https://kulinaria.ge/receptebi/cat/comeuli/?page=1"]
    BASE_URL = "https://kulinaria.ge"
    max_pages = 5  # Set this to whatever the maximum number of pages is

    def parse(self, response):
        # Get all recipes listed on the page
        recipes = response.css("div.kulinaria-row.box-container div.box--massonry")

        for recipe in recipes:
            recipe_link = recipe.css("a.box__title::attr(href)").get()
            full_link = response.urljoin(recipe_link) if recipe_link else None

            # Basic recipe information
            yield {
                "title": recipe.css("a.box__title::text").get("").strip(),
                "description": recipe.css("div.box__desc::text")
                .get("Description not found")
                .strip(),
                "recipe_link": full_link,
                "image": response.urljoin(
                    recipe.css("div.box__img img::attr(src)").get("Image not found")
                ),
                "author": recipe.css("div.box__author a::text").get("Unknown"),
                "rating": len(recipe.css("div.post-star__item.act")),
            }

            # If the recipe link is valid, follow it to extract more detailed information
            if full_link:
                yield scrapy.Request(full_link, callback=self.parse_full_recipe)

        # Pagination: manually increment page number and follow to the next page if it exists
        current_page = int(re.search(r"page=(\d+)", response.url).group(1))
        if current_page < self.max_pages:
            next_page = (
                f"{self.BASE_URL}/receptebi/cat/comeuli/?page={current_page + 1}"
            )
            yield scrapy.Request(url=next_page, callback=self.parse)

    def parse_full_recipe(self, response):
        # Extract ingredients
        ingredients = response.css("div.list__item::text").getall()

        # Extract steps
        steps = []
        for step in response.css("div.lineList__item"):
            step_number = step.css("div.count::text").get().strip()
            step_description = step.css("p::text").get().strip()
            steps.append({"step_number": step_number, "description": step_description})

        # Extract portion count (using class .kulinaria-sprite--circleprogress)
        portion = response.css(
            "div.lineDesc__item .kulinaria-sprite--circleprogress + ::text"
        ).re_first(r"(\d+)")

        # Extract subcategory link (from pagination container)
        subcategory_link = response.css(
            "div.pagination-container a.pagination__item:last-child::attr(href)"
        ).get()

        # Construct full subcategory link using BASE_URL
        full_subcategory_link = (
            f"{self.BASE_URL}{subcategory_link}" if subcategory_link else None
        )

        recipe = {
            "ingredients": ingredients,
            "steps": steps,
            "portion": portion,
            "subcategory_link": full_subcategory_link,
        }

        # Clean the final recipe data and yield it to be processed by the pipeline
        yield self.clean_recipe_data(recipe)

    @staticmethod
    def clean_recipe_data(recipe):
        # Clean ingredients
        clean_ingredients = []
        for ingredient in recipe["ingredients"]:
            clean_ingredient = re.sub(r"\s+", " ", ingredient).strip()
            if clean_ingredient and clean_ingredient not in ["/", "⁄"]:
                clean_ingredients.append(clean_ingredient)
        recipe["ingredients"] = clean_ingredients

        # Clean steps
        for step in recipe["steps"]:
            step["description"] = re.sub(r"\s+", " ", step["description"]).strip()

        # Clean portion (ensure it's None if not available)
        recipe["portion"] = recipe["portion"] if recipe["portion"] else None

        # Clean subcategory link (ensure it's None if not available)
        recipe["subcategory_link"] = (
            recipe["subcategory_link"] if recipe["subcategory_link"] != "#" else None
        )

        return recipe
