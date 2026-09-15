SITE_URL = "http://localhost:5000"

TOOLS = {
    "pdf-to-word": {
        "title": "PDF to Word Converter — मुफ़्त ऑनलाइन कन्वर्टर",
        "h1": "PDF to Word Converter",
        "meta_description": "अपनी PDF फ़ाइलों को एडिटेबल Word (DOCX) दस्तावेज़ में तुरंत बदलें।",
        "endpoint": "/api/pdf-to-word",
        "accept": ".pdf",
        "outname": "converted.docx",
        "has_quality": False,
        "has_target_kb": False,
        "button_text": "Word में बदलें",
        "intro": "बिना किसी फॉर्मेटिंग लॉस के अपनी PDF फ़ाइलों को एडिटेबल Word दस्तावेज़ में बदलें।",
        "faq": [
            ("क्या मेरी फाइलें सुरक्षित हैं?", "हाँ, कन्वर्शन के तुरंत बाद फाइलें सर्वर से डिलीट कर दी जाती हैं।"),
            ("क्या यह सेवा पूरी तरह मुफ्त है?", "हाँ, आप बिना किसी शुल्क के कितनी भी फाइलें कन्वर्ट कर सकते हैं।")
        ]
    },
    "word-to-pdf": {
        "title": "Word to PDF Converter — ऑनलाइन DOCX से PDF",
        "h1": "Word to PDF Converter",
        "meta_description": "Word (DOC/DOCX) फ़ाइलों को हाई-क्वालिटी PDF फॉर्मेट में बदलें।",
        "endpoint": "/api/word-to-pdf",
        "accept": ".doc,.docx",
        "outname": "converted.pdf",
        "has_quality": False,
        "has_target_kb": False,
        "button_text": "PDF में बदलें",
        "intro": "अपने Word दस्तावेज़ों को सुरक्षित और प्रिंट-फ्रेंडली PDF फ़ाइल में बदलें।",
        "faq": [
            ("क्या DOC और DOCX दोनों सपोर्टेड हैं?", "हाँ, यह दोनों प्रारूपों को सपोर्ट करता है।")
        ]
    },
    "pdf-compress": {
        "title": "Compress PDF Online — PDF का साइज़ कम करें",
        "h1": "PDF Compress करें",
        "meta_description": "PDF फ़ाइल का साइज़ गुणवत्ता खोए बिना घटाएं (100KB, 200KB, 500KB)।",
        "endpoint": "/api/pdf-compress",
        "accept": ".pdf",
        "outname": "compressed.pdf",
        "has_quality": True,
        "has_target_kb": True,
        "button_text": "Compress करें",
        "intro": "ऑनलाइन फ़ॉर्म और ईमेल के लिए अपनी PDF फ़ाइलों का साइज़ सेकंडों में छोटा करें।",
        "faq": [
            ("क्या कंप्रेशन से टेक्स्ट धुंधला होगा?", "नहीं, हमारा सिस्टम टेक्स्ट की स्पष्टता बनाए रखता है।")
        ]
    },
    "image-to-word": {
        "title": "Image to Word Converter (OCR) — फ़ोटो से टेक्स्ट निकालें",
        "h1": "Image to Word Converter",
        "meta_description": "तस्वीरों (JPG, PNG) से हिंदी और अंग्रेज़ी टेक्स्ट निकालकर Word बनाएं।",
        "endpoint": "/api/image-to-word",
        "accept": "image/*",
        "outname": "extracted.docx",
        "has_quality": False,
        "has_target_kb": False,
        "button_text": "Text निकालें",
        "intro": "स्कैन किए गए दस्तावेज़ों या फ़ोटो से सीधे एडिटेबल Word फ़ाइल प्राप्त करें।",
        "faq": [
            ("क्या यह हिंदी भाषा पहचान सकता है?", "हाँ, इसमें हिंदी और अंग्रेज़ी दोनों भाषाओं का OCR सपोर्ट है।")
        ]
    },
    "image-to-excel": {
        "title": "Image to Excel Converter (OCR) — टेबल फ़ोटो से Excel",
        "h1": "Image to Excel Converter",
        "meta_description": "तस्वीरों में मौजूद डेटा और टेबल्स को सीधे Excel (XLSX) स्प्रेडशीट में बदलें।",
        "endpoint": "/api/image-to-excel",
        "accept": "image/*",
        "outname": "extracted.xlsx",
        "has_quality": False,
        "has_target_kb": False,
        "button_text": "Excel में बदलें",
        "intro": "डेटा और रसीदों की तस्वीरों को दोबारा टाइप करने के बजाय सीधे Excel में बदलें।",
        "faq": [
            ("क्या जटिल टेबल्स का डेटा सही आएगा?", "साफ़ और स्पष्ट बॉर्डर वाली तस्वीरों में यह सबसे सटीक परिणाम देता है।")
        ]
    }
}

COMPRESS_SIZE_PAGES = {
    "compress-pdf-to-100kb": {
        "title": "Compress PDF to 100KB Online Free",
        "h1": "Compress PDF to 100KB",
        "meta_description": "अपनी PDF फ़ाइल का साइज़ 100KB के अंदर लाएं।",
        "target_kb": 100,
        "intro": "सरकारी और जॉब फॉर्म्स के लिए अपनी PDF फ़ाइल को 100KB तक कंप्रेस करें।"
    },
    "compress-pdf-to-200kb": {
        "title": "Compress PDF to 200KB Online Free",
        "h1": "Compress PDF to 200KB",
        "meta_description": "अपनी PDF फ़ाइल का साइज़ 200KB के अंदर लाएं।",
        "target_kb": 200,
        "intro": "विभिन्न ऑनलाइन पोर्टल्स के लिए अपनी PDF को 200KB तक सुरक्षित रूप से कंप्रेस करें।"
    },
    "compress-pdf-to-500kb": {
        "title": "Compress PDF to 500KB Online Free",
        "h1": "Compress PDF to 500KB",
        "meta_description": "अपनी PDF फ़ाइल का साइज़ 500KB के अंदर लाएं।",
        "target_kb": 500,
        "intro": "बड़ी PDF फ़ाइलों को ईमेल या वेबसाइट अपलोड के लिए 500KB तक छोटा करें।"
    },
    "compress-pdf-to-1mb": {
        "title": "Compress PDF to 1MB Online Free",
        "h1": "Compress PDF to 1MB",
        "meta_description": "अपनी PDF फ़ाइल का साइज़ 1MB के अंदर लाएं।",
        "target_kb": 1024,
        "intro": "भारी PDF फ़ाइलों का साइज़ 1MB के अंदर लाएं।"
    }
}

