from youtube_transcript_api import YouTubeTranscriptApi
from sentence_transformers import SentenceTransformer
import chromadb
from ollama import chat 
import time
from vectorDB import get_collection

def create_chunk(full_text,chunk_size = 1000,overlap = 100):
    chunks = []
    start = 0
    while start < len(full_text):
        end = start + chunk_size

        chunk = full_text[start:end]

        chunks.append(chunk)

        start = end - overlap
    
    return chunks

url = input("Enter Youtube Url : ")

video_id = url.split("v=")[1].split("&")[0]

print(video_id)

api = YouTubeTranscriptApi()

# Transcript ko text me convert
try:
    transcript = api.fetch(video_id,languages=["hi"])
except:
    try:
        transcript = api.fetch(video_id, languages=["en-IN"])

    except:
        transcript = api.fetch(video_id, languages=["en"])




full_text = ""

for item in transcript:
    full_text += item.text + " "

# chunking
chunked = create_chunk(full_text)

#embedding

model = SentenceTransformer("all-MiniLM-L6-v2")



#DB

collection = get_collection()

if collection.count() == 0:
    print("creating embedding...")
    embedding = model.encode(chunked)

    for i,chunk in enumerate(chunked):

        collection.add(
            documents=[chunk],
            ids=[str(i)],
            embeddings=[embedding[i].tolist()]
        )

else:
    print("using save embedding")


while True:
    user = input("You : ")

    if user.lower() in ["bye","by","end","exit"]:
        print("GoodBye👋")
        break

    user_embedding = model.encode(user).tolist()

    result = collection.query(
        query_embeddings = [user_embedding],
        n_results=3
        )
    
    context = "\n".join(result["documents"][0])

    #prompt Engineering

    prompt = f'''
            You are a helpful AI assistant who is ready to help everyone

            Answer the question only from the given context
            {context}

            Give an easy and understandable answer
            {user}

            at last you should give some suggestiona and recommended question related to context '''
    
    response = chat(
        model='llama3',
        messages=[
            {
                'role': 'user',
                'content': prompt
            }
        ]
    )

    bot_reply = response['message']['content']

    print("Yt Chat: ",end="")
    for i in bot_reply:
        print(i,end="",flush=True)
        time.sleep(0.002)
    print("\n")
