from fastapi import FastAPI, Depends, Header, HTTPException

app = FastAPI()

def get_token_header(x_token: str = Header(...)):
    if x_token != "expected-token":
        raise HTTPException(status_code=400, detail="Invalid token")
    return x_token

@app.get("/check")
def check_token(token: str = Depends(get_token_header)):
    return {"token": token}
