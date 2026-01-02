from fastapi import FastAPI
app = FastAPI(
    title="My FastAPI Application",
    description="This is a sample FastAPI application.",
    version="1.0.0",
    doc_url="/doc",
    redoc_url="/redoc"
)
@app.get("/")
def say():
    """
    this is api for testing purpose
    """
    return {"message": "welcome to api learning Aliya"}
