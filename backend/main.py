from fastapi import FastAPI

app = FastAPI() 

@app.get("/")
def home(): 
    return {"message": "Local AI Search Enginer backend is running"}