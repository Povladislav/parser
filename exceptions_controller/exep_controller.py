# from fastapi import FastAPI, Request
# from fastapi.responses import JSONResponse
# from schemas.user import clothEntity
#
#
# class UnicornException(Exception):
#     def __init__(self, cloths: str):
#         self.clothes = cloths
#
#
# app = FastAPI()
#
#
# @app.exception_handler(UnicornException)
# async def unicorn_exception_handler(request: Request, exc: UnicornException):
#     return JSONResponse(
#         status_code=418,
#         content={"message": f"Oops! {exc.clothes} did something. There goes a rainbow..."})
