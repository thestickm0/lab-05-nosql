#!/usr/bin/env python3

import logging
import os
from pymongo import MongoClient
from pymongo.errors import PyMongoError


MONGODB_ATLAS_URL = os.getenv("MONGODB_ATLAS_URL")
MONGODB_ATLAS_USER = os.getenv("MONGODB_ATLAS_USER")
MONGODB_ATLAS_PWD = os.getenv("MONGODB_ATLAS_PWD")

author_ids = ['author_001','author_002','author_003','author_004','author_005']


logging.basicConfig(level=logging.INFO,format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)
#Logging stuff, used Claude to figure out how to set it up

def print_books(authors,books,author_id):
    """Prints an author's name and their books.

    Args:
        authors (list): list of authors
        books (list): list of books
        author_id (string): Identifies which author gets printed
    """
    author = authors.find_one({"_id":author_id})
    if author is None:
        logger.warning("No author found with _id %s", author_id)
        return

    print(author['name'])
    for book in books.find({"author_ids": author["_id"]}):
        #every book whose author_ids array contains this author's _id
        print(f"  {book['title']} ({book['published_year']})")
    return

def main():
    """Connects to MongoDB, connects to bookstore database, returns authors and books
    """
    if not all([MONGODB_ATLAS_URL,MONGODB_ATLAS_USER,MONGODB_ATLAS_PWD]):
        logger.error("URL, user, or password is incorrect")
        return

client = None
try:
    client = MongoClient(MONGODB_ATLAS_URL,username = MONGODB_ATLAS_USER,password = MONGODB_ATLAS_PWD,connectTimeoutMS=200,retryWrites=True)
    


    client.admin.command("ping") #Connects to Atlas
    logger.info("Connected to MongoDB Atlas")
    db = client["bookstore"] #gets databse
    authors = db["authors"] # get list of authors
    books = db["books"] # get list of books
    count = authors.count_documents({"_id": {"$in": author_ids}}) # Counts how many authors exist in the collection
    print(f"Authors {count}\n")
    #Loop over the list, keeps it in order
    for author_id in author_ids:
        print_books(authors,books,author_id)

except PyMongoError as err:
    logger.error("MongoDB error: %s", err)
    #Error message

finally:
    #Closing the client
    if client is not None:
        client.close()
        logger.info("Connection closed")


if __name__ == "__main__":
    main()


    