from fastapi import FastAPI
from checker import check_drift

app = FastAPI()

@app.get("/run-check")
def run_check():
    return check_drift("http://127.0.0.1:8001/student")