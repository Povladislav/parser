import uvicorn
from fastapi import FastAPI

from routes.cloth import cloth
from routes.stream import stream

app = FastAPI()
app.include_router(cloth)
app.include_router(stream)

# if __name__ == "__main__":
#     uvicorn.run("parser.main:app", host="0.0.0.0", port=8000, reload=True)
