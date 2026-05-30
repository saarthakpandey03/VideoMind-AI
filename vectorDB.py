import chromadb

def get_collection():

    client = chromadb.PersistentClient(
        path="./myDB"
    )

    collection = client.get_or_create_collection(
        name="youtube_data"
    )

    return collection