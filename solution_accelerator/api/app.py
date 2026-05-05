from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from solution_accelerator.core.orchestrator import run_pipeline

app = FastAPI()

# ✅ Enable React → FastAPI communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # later restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"message": "API is running"}


@app.post("/run")
def run(data: dict):
    """
    Handles BOTH:
    1. {"text": "Need SS316 pipes"}
    2. {"category": "pipes", ...}
    """
    input_data = data.get("text", data)
    return run_pipeline(input_data)
