from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/status")
async def get_status():
    return JSONResponse(content={"status":"ok", "message":"API is running!"})