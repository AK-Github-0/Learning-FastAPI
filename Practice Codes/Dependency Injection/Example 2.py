from fastapi import Depends, FastAPI

app = FastAPI()


class MyConfig:
    def __init__(self):
        self.setting = "value"

def get_config():
    return MyConfig()

@app.get("/config")
def read_config(cfg: MyConfig = Depends(get_config)):
    return {"setting": cfg.setting}

def get_name():
    return "Alice"

@app.get("/greet")
def greet_user(name: str = Depends(get_name)):
    return {"message": f"Hello {name}"}
