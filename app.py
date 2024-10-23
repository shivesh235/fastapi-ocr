from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pytesseract import image_to_string
from PIL import Image
import io

app = FastAPI()

# Serve static files (like HTML)
# app.mount("/static", StaticFiles(directory="static"), name="static")

# HTML frontend to upload images
@app.get("/", response_class=HTMLResponse)
async def main():
    return """
    <html>
        <body>
            <h1>Upload an image for OCR</h1>
            <form action="/upload-image/" enctype="multipart/form-data" method="post">
                <input name="file" type="file">
                <input type="submit">
            </form>
        </body>
    </html>
    """

# OCR processing route
@app.post("/upload-image/")
async def upload_image(file: UploadFile = File(...)):
    contents = await file.read()
    image = Image.open(io.BytesIO(contents))
    ocr_text = image_to_string(image)
    return {"ocr_text": ocr_text}
