from pymongo import MongoClient

def db_setup():
    client = MongoClient("mongodb://localhost:27017/")
    db = client['recipes_database']
    collection = db['recipes']
    return collection

collection = db_setup()

def get_average_recipe_count():

    documents = collection.find({}, {'_id':0 , "ingredients": 1})
    recipe_count = 0
    result = 0
    for document in documents:
        recipe_count += 1
        result += len(document['ingredients'])
    return round(result/recipe_count,2)

def get_average_steps_to_cook():

    documents = collection.find({}, {'_id':0 , "steps": 1})
    recipe_count = 0
    result = 0
    for document in documents:
        recipe_count += 1
        result += len(document['steps'])
    return round(result/recipe_count ,2)


def get_recipe_with_most_portion():
    documents = collection.find({}, {'_id':0 ,"title": 1 , "recipe_link": 1})
    result =documents.sort("portion_count",-1)[0]
    return result

def get_author_with_most_recipes():
    result = collection.aggregate([
        {
            "$group": {
                "_id": "$author",
                "recipe_count": {"$sum": 1}
            }
        },
        {
            "$sort": {
                "recipe_count": -1
            }
        },
        {
            "$limit":1
        }
    ])
    if result:
        return list(result)[0]["_id"]
    return None
