from fastapi import FastAPI
from fastapi import Header
from fastapi import HTTPException
from fastapi import status
from fastapi import Depends

from typing import Annotated

app = FastAPI()

# Add dependencies to the path operation decorator
async def verify_token(x_token: Annotated[str, Header()]):
  if x_token != "fake-super-secret-token":
    raise HTTPException(
      status_code = status.HTTP_400_BAD_REQUEST,
      detail = "X-Token header invalid"
    )

  return x_token

async def verify_key(x_key: Annotated[str, Header()]):
  if x_key != "":
    raise HTTPException(
      status_code = status.HTTP_400_BAD_REQUEST,
      detail = "X-Key header invalid"
    )

  return x_key

@app.get("/items", dependencies = [Depends(verify_token), Depends(verify_key)])
async def read_items():
  return [
    {"item": "Foo"},
    {"item": "Bar"}
  ]
