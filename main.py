import uvicorn
from fastapi import FastAPI

from routes.user import user

app = FastAPI()
app.include_router(user)
#
# if __name__ == "__main__":
#     uvicorn.run("parser.main:app", host="0.0.0.0", port=8000, reload=True)
