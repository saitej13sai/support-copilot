from fastapi import FastAPI
from api.issue_api import router

app = FastAPI()

# Root route
@app.get("/")
def read_root():
    return {"message": "Welcome to Support Copilot API! Use /docs to explore endpoints."}

# Include the issue_api routes
app.include_router(router)
