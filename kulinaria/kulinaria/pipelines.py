import pymongo
import logging


class MongoDBPipeline:
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        # Pull settings from Scrapy settings
        return cls(
            mongo_uri=crawler.settings.get("MONGO_URI"),
            mongo_db=crawler.settings.get("MONGO_DATABASE", "recipes_database"),
        )

    def open_spider(self, spider):
        # Initialize MongoDB connection when spider is opened
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]
        self.collection = self.db["recipes"]  # Define the collection
        logging.info(f"Connected to MongoDB database: {self.mongo_db}")

    def close_spider(self, spider):
        # Close MongoDB connection when spider is closed
        self.client.close()
        logging.info("MongoDB connection closed.")

    def process_item(self, item, spider):
        # Log the item being processed
        logging.info(f"Processing item: {item}")

        # Insert or update scraped data into MongoDB
        self.collection.update_one(
            {"recipe_link": item.get("recipe_link")},
            {"$set": item},
            upsert=True
        )
        return item
