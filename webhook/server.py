from fastapi import FastAPI, Request
import subprocess

app = FastAPI()

@app.post("/github-webhook")
async def github_webhook(request: Request):
    data = await request.json()
    if data.get("ref", "").endswith("main"):  # Trigger only for main branch
        subprocess.Popen(["/home/adqdevops2/webhook/pull_and_trigger.sh"])
        return {"status": "Triggered DAG"}
    return {"status": "Not main branch"}

