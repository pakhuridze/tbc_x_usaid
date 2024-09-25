# Recipes Scraper

This project is a web scraper for gathering recipes from the Georgian website [kulinaria.ge](https://kulinaria.ge), processing them, and storing them in a MongoDB database. It also includes several queries for analyzing the collected data.

## Features
- Scrapes recipe data, including:
  - Title
  - URL
  - Category
  - Subcategory
  - Image
  - Short description
  - Author
  - Servings
  - Ingredients
  - Preparation steps
- Stores the scraped data in a MongoDB database.
- Performs statistical analysis:
  - Average ingredients per recipe.
  - Average preparation steps per recipe.
  - Recipe with the most servings.
  - Author with the most published recipes.

## Installation

### Requirements
- Python 3.x
- MongoDB
- Required Python packages in `requirements.txt`

### Setup Instructions
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/recipes_scraper.git
    ```
2. Navigate into the project directory:
    ```bash
    cd recipes_scraper
    ```
3. Create and activate a virtual environment:
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # For Linux/Mac
    .\.venv\Scripts\activate   # For Windows
    ```
4. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### MongoDB Setup
1. Ensure MongoDB is installed and running locally or on a cloud service.
2. Modify the default MongoDB connection string in the code if necessary.

## Usage

1. To analyze the data:
    ```bash
    python main.py
    ```

## Project Structure

```
recipes_scraper/
│
├── .idea/                  # IDE settings (optional)
├── .venv/                  # Virtual environment
├── main.py                 # Entry point for scraping
├── parser.py               # parsing
├── data_fetching.py        # database setup and queries
├── README.md               # This file
├── requirements.txt        # Python dependencies
└── .gitignore              # Files ignored by Git
```

## Queries in `data_fetching.py`

- **Average ingredients per recipe**: Prints the average number of ingredients.
- **Average preparation steps per recipe**: Displays the average number of preparation steps.
- **Recipe with the most servings**: Shows the recipe with the highest serving size.
- **Author with the most published recipes**: Finds the author with the most recipes.

## Contributing
Feel free to contribute by submitting pull requests or reporting issues.

## License
This project is licensed under the MIT License.
