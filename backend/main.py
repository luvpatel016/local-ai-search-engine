from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

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

@app.get("/upload")
async def upload_file(file: UploadFile = File(...)):
    return {"filename": file.filename}

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    return {"filename": file.filename}