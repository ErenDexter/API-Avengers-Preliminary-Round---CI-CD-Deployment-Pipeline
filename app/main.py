from fastapi import FastAPI, Response
import uvicorn

app = FastAPI()

@app.get("/")
def index():
    return Response(content="Hello, World!", media_type="text/plain", status_code=200)

@app.get("/health")
def health():
    return Response(content='Ok', media_type="application/json", status_code=200)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)