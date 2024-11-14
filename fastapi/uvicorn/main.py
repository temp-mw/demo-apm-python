import logging

from middleware import mw_tracker, MWOptions
mw_tracker(
    MWOptions(
        access_token="whkvkobudfitutobptgonaezuxpjjypnejbb",
        target="https://myapp.middleware.io:443",
        service_name="MyPythonApp",
    )
)


from dotenv import load_dotenv
load_dotenv()
import os

from typing import Union

from fastapi import FastAPI

app = FastAPI()

logging.getLogger().setLevel(logging.INFO)

@app.get("/")
def read_root():
    logging.info("Hello World")
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    logging.debug("Item ID: %s", item_id)
    return {"item_id": item_id, "q": q}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run('main:app', reload=True)