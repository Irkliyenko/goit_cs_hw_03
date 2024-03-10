import argparse
from pymongo import MongoClient, errors
from pymongo.server_api import ServerApi

# Initialize the MongoDB connection.
try:
    client = MongoClient(
        "mongodb+srv://<username>:<password>@", server_api=ServerApi('1'))
    db = client.book  # Specify your database name here.
except errors.ConnectionFailure:
    print("Failed to connect to MongoDB. Check your connection string and server status.")
    exit(1)

parser = argparse.ArgumentParser(description="Cat Database Management")
parser.add_argument(
    "--action", help="create, show all, find, add, update, delete, delete all")
parser.add_argument("-pk",  help="id", action="store_true")
parser.add_argument("-n", "--name", help="Cat name")
parser.add_argument("-a", "--age", help="Cat age")
parser.add_argument("-f", "--features", help="Cat features", nargs='+')

args = vars(parser.parse_args())

action = args["action"]
# pk = args["id"]
name = args["name"]
age = args["age"]
features = args["features"]


def show_all_cats():
    # Display all cat documents in the 'cats' collection.
    try:
        result = db.cats.find()
        [print(cat) for cat in result]
    except Exception as e:
        # Handle any errors that occur during the find operation.
        print(f"An error occurred: {e}")


def find_cat_by_name(name):
    # Find and display a specific cat document by name.
    try:
        result = db.cats.find_one({'name': name})
        if result:
            print(result)
        else:
            print(f"No cat found with the name {name}")
    except Exception as e:
        # Handle any errors that occur during the find operation.
        print(f"An error occurred: {e}")


def create(name, age, features):
    # Create a new cat document with the given name, age, and features.
    try:
        result = db.cats.insert_one(
            {'name': name, 'age': int(age), 'features': features})
        print(f"Created new cat: {name}")
    except Exception as e:
        # Handle any errors that occur during the insert operation.
        print(f"An error occurred: {e}")


def update_age(name, age):
    # Update the age of a specific cat document by name.
    try:
        if not age.isdigit():
            # Validate that the new age is a digit before attempting to update.
            print("Please enter a valid age.")
            return
        new_age = int(age)
        result = db.cats.update_one(
            {'name': name}, {'$set': {'age': new_age}})
        if result.matched_count > 0:
            print(f"Updated {name}'s age to {new_age}.")
        else:
            print(f"No cat found with the name {name}")
    except Exception as e:
        # Handle any errors that occur during the update operation.
        print(f"An error occurred: {e}")


def add_features(name, features):
    # Add a new feature to a specific cat document's features list.
    try:
        result = db.cats.update_one(
            {'name': name}, {"$addToSet": {"features": features}})
        if result.matched_count > 0:
            print(f"Added feature(s) to {name}.")
        else:
            print(f"No cat found with the name {name}")
    except Exception as e:
        # Handle any errors that occur during the update operation.
        print(f"An error occurred: {e}")


def delete_one(name):
    # Delete a specific cat document by name.
    try:
        result = db.cats.delete_one({'name': name})
        if result.deleted_count > 0:
            print(f"Deleted {name}.")
        else:
            print(f"Cat not found")
    except Exception as e:
        # Handle any errors that occur during the delete operation.
        print(f"An error occurred: {e}")


def delete_all():
    # Delete all cat documents in the 'cats' collection.
    try:
        result = db.cats.delete_many({})
        print(f"Deleted {result.deleted_count} cats.")
    except Exception as e:
        # Handle any errors that occur during the delete operation.
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    match action:
        case 'show_all':
            show_all_cats()
        case 'find':
            find_cat_by_name(name)
        case 'update':
            update_age(name, age)
        case 'add':
            add_features(name, features)
        case 'delete':
            delete_one(name)
        case 'delete_all':
            delete_all()
        case 'create':
            create(name, age, features)
