from fastapi import FastAPI

from .routers import items

app = FastAPI()

app.include_router(items.router)

@app.get('/')
async def root():
  return {'message': 'Hello World!'}


"""
Note:
If you want run the project make sure this main program inside 'api' directory
example: uvicorn api.main:app --reload
"""