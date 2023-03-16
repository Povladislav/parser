import uvicorn
from fastapi.responses import JSONResponse
from fastapi import FastAPI, Request
from exceptions_controller.exep_controller import UnicornException
from routes.cloth import cloth
from routes.stream import stream

app = FastAPI()
app.include_router(cloth)
app.include_router(stream)


@app.exception_handler(UnicornException)
async def unicorn_exception_handler(request: Request, exc: UnicornException):
    return JSONResponse(
        status_code=404,
        content={"message": f"Oops! {exc.page} is not available! User positive page number!"})

# if __name__ == "__main__":
#     uvicorn.run("parser.main:app", host="0.0.0.0", port=8000, reload=True)
