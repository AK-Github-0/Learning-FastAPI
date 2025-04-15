from fastapi import Depends, FastAPI

app = FastAPI()

def common_parameters(q: str = None, page: int = 1, limit: int = 10):
    return {"q": q, "page": page, "limit": limit}

@app.get("/items/")
def read_items(commons: dict = Depends(common_parameters)):
    return commons
