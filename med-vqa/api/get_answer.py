from fastapi import FastAPI, File, Form, UploadFile
from fastapi.responses import JSONResponse
from io import BytesIO
from PIL import Image

app = FastAPI()

@app.post("/")
async def get_answer(image: UploadFile = File(...), question: str = Form(...)):
    img_bytes = await image.read()
    img = Image.open(BytesIO(img_bytes))

    # Simulated answer (Replace with real model inference)
    answer = f"Answer for '{question}' (mock)"
    return JSONResponse(content={"answer": answer})