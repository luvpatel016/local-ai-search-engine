from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI() 

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home(): 
    return {"message": "Local AI Search Engine backend is running"}

@app.get("/search")
def search(query: str):
    return {"query_received": query}

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):

    file_path = os.path.join("..", "documents", file.filename)

    contents = await file.read()

    with open(file_path, "wb") as saved_file:
        saved_file.write(contents)

    return {
        "filename": file.filename,
        "message": "File uploaded successfully"
    }