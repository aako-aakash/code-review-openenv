from fastapi import FastAPI
import uvicorn
from env.environment import CodeReviewEnv
from env.models import Action
import subprocess
app = FastAPI()
env = CodeReviewEnv()

@app.get("/")
def home():
    return {
        "message": "Code Review OpenEnv is running 🚀",
        "endpoints": ["/reset", "/step", "/state"]
    }


@app.post("/reset")
def reset():
    obs = env.reset()
    return obs.dict()


@app.post("/step")
def step(action: dict):
    action_obj = Action(**action)
    result = env.step(action_obj)
    return result.dict()


@app.get("/state")
def state():
    return env.state()


#  REQUIRED MAIN FUNCTION
def main():
    uvicorn.run("server.app:app", host="0.0.0.0", port=8000, reload=False)


#  REQUIRED ENTRY POINT
if __name__ == "__main__":
    main()

if __name__ == "__main__":
    subprocess.run(["python", "inference.py"])