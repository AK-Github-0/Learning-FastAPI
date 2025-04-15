from fastapi import FastAPI, Depends, Header, HTTPException

app = FastAPI()

class CommonParams:
    def __init__(self, q: str = None, page: int = 1, limit: int = 10):
        self.q = q
        self.page = page
        self.limit = limit

@app.get("/items/")
def read_items(commons: CommonParams = Depends()):
    return {"q": commons.q, "page": commons.page, "limit": commons.limit}

class TokenChecker:
    def __init__(self, x_token: str = Header(...)):
        self.x_token = x_token

    def __call__(self):
        if self.x_token != "secret":
            raise HTTPException(status_code=403, detail="Bad token")
        return {"auth": True}

@app.get("/verify")
def verify_user(auth=Depends(TokenChecker)):
    return auth

class AuthService:
    def __init__(self, token: str = Header(...)):
        self.token = token

    def __call__(self):
        if self.token != "expected-token":
            raise HTTPException(status_code=403, detail="Unauthorized")
        return {"user": "admin"}

@app.get("/secure")
def secure_route(user = Depends(AuthService)):
    return user
