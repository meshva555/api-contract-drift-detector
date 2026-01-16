from fastapi import FastAPI

app = FastAPI()

@app.get("/student")
def get_student():
    return {
        "name": "Rahul",
        "roll_number": "101",
        "phone": "9999999999"
    }
