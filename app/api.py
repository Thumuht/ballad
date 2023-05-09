from fastapi import FastAPI

app = FastAPI()

sessions = dict()
users = dict()

@app.get("/")
async def root() -> dict:
    return {"message": "Hello World"}

# register
@app.post("/register/{username}/{password}")
async def register(username: str, password: str) -> dict:
    if username in users:
        return {"message": "username already exists"}
    else:
        users[username] = password
        return {"message": "register"}
    
# query whether successfully login
@app.get("/login/{username}")
async def login(username: str) -> dict:
    return {"online": f"{username in sessions}"}

@app.post("/logout/{username}")
async def logout(username: str) -> dict:
    if username in sessions:
        del sessions[username]
        return {"message": "logout"}
    else:
        return {"message": "not logged in"}

@app.post("/login/{username}/{password}")
async def login(username: str, password: str) -> dict:
    if username in users:
        if users[username] == password:
            sessions[username] = True
            return {"message": "login"}
        else:
            return {"message": "wrong password"}
    else:
        return {"message": "username not found"}
