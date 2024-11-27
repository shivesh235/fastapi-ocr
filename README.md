# **OCR Web Application** 📄➡️🖥️

This is a **FastAPI-based OCR (Optical Character Recognition)** web application that allows users to extract text from uploaded images. The app utilizes the **Tesseract OCR Engine** to convert text within images into a readable format.

---

## **Features**
1. **Upload Images**:  
   - Users can upload image files in formats such as PNG, JPEG, etc.
   
2. **Extract Text**:  
   - Automatically extracts text from the uploaded image using the Tesseract OCR engine.
   
3. **Image Display**:  
   - Displays the uploaded image and the extracted text on the result page.

4. **Error Handling**:  
   - Validates file types and provides meaningful error messages for unsupported formats or other issues.

5. **Responsive Web Design**:  
   - HTML templates and CSS styling ensure a user-friendly interface.

---

## **How It Works**
1. **Upload an Image**:  
   Navigate to the homepage, upload an image using the provided form, and submit.

2. **OCR Process**:  
   The app processes the image using the **`pytesseract`** library and extracts any text detected in the image.

3. **Display Results**:  
   After processing, the extracted text and the uploaded image are displayed on the page.

4. **Handle Errors**:  
   If no text is found or an invalid file is uploaded, the app will notify the user.

---

## **Project Structure**
```plaintext
├── app.py                # Main FastAPI application
├── templates/
│   ├── index.html        # HTML template for the web interface
├── static/
│   ├── styles.css        # CSS file for styling the app
├── requirements.txt      # Python dependencies
```

---

## **Installation**
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/ocr-web-app.git
   cd ocr-web-app
   ```

2. **Install Dependencies**:
   Use a virtual environment and install the required libraries.
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Install Tesseract**:
   Ensure that Tesseract OCR is installed on your system.  
   [Installation Guide](https://github.com/tesseract-ocr/tesseract)

4. **Run the Application**:
   ```bash
   uvicorn app:app --reload
   ```

5. **Access the Web App**:  
   Open your browser and navigate to `http://127.0.0.1:8000`.

---

## **Dependencies**
- **FastAPI**: For building the web application.
- **Jinja2**: For HTML templating.
- **Pillow**: For image processing.
- **pytesseract**: For performing OCR.
- **Tesseract OCR**: The backend OCR engine (must be installed separately).

---

## **Templates**
### **index.html**
The main page allows users to:
- Upload an image.
- View extracted text and uploaded image after submission.

---

## **Future Enhancements**
- Support for multi-language OCR.
- Integration of advanced OCR techniques like handwriting recognition.
- Display text confidence scores for OCR results.
- API endpoint for programmatic OCR extraction.

---

Feel free to contribute to the repository or use this app as a foundation for more advanced OCR-based applications! 😊