FROM python:3.11-slim

# System dependencies: LibreOffice (Word->PDF), Tesseract OCR (Image tools), Ghostscript (Compress)
RUN apt-get update && apt-get install -y --no-install-recommends \
    libreoffice \
    tesseract-ocr \
    tesseract-ocr-hin \
    poppler-utils \
    ghostscript \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# पहले requirements कॉपी करके इंस्टॉल करें ताकि Docker caching का लाभ मिले
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# पूरा प्रोजेक्ट कोड कॉपी करें
COPY . .

# टेम्परेरी फ़ोल्डर्स तैयार करें
RUN mkdir -p uploads outputs

EXPOSE 5000

# प्रोडक्शन सर्वर Gunicorn चलाएं
CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0:5000", "--timeout", "120", "app:app"]
```[span_0](start_span)[span_0](end_span)

---

**चलाने के कमांड्स (Terminal / Command Prompt में):**

* **इमेज बिल्ड करें:**
  ```bash
  docker build -t filetools .

