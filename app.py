from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pytesseract import image_to_string
from PIL import Image
import io
import base64
from starlette.requests import Request

app = FastAPI(title="OCR Web App", description="Extract text from images using OCR")

# Mount the static directory (for CSS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates for rendering HTML pages
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def main(request: Request):
    return templates.TemplateResponse("index.html", {
        "request": request,
        "title": "OCR Image to Text Converter"
    })

@app.post("/upload-image/")
async def upload_image(request: Request, file: UploadFile = File(...)):
    try:
        # Validate file type
        if not file.content_type.startswith('image/'):
            raise HTTPException(status_code=400, detail="File must be an image")
        
        contents = await file.read()
        image = Image.open(io.BytesIO(contents))
        
        # Convert image to text using pytesseract
        ocr_text = image_to_string(image)
        
        # If no text was extracted
        if not ocr_text.strip():
            ocr_text = "No text was detected in the image."

        # Convert image to base64 to display on the HTML page
        img_byte_arr = io.BytesIO()
        image.save(img_byte_arr, format=image.format or "PNG")
        img_byte_arr = img_byte_arr.getvalue()
        img_base64 = base64.b64encode(img_byte_arr).decode('utf-8')

        return templates.TemplateResponse("index.html", {
            "request": request,
            "title": "OCR Image to Text Converter",
            "ocr_text": ocr_text,
            "image_data": img_base64,
            "filename": file.filename
        })
        
    except Exception as e:
        return templates.TemplateResponse("index.html", {
            "request": request,
            "title": "OCR Image to Text Converter",
            "error": f"An error occurred: {str(e)}"
        })