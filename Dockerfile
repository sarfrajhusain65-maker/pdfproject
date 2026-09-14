<!DOCTYPE html>
<html lang="hi">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />

<title>{% block title %}FileTools — PDF, Word, Excel Converter{% endblock %}</title>
<meta name="description" content="{% block meta_description %}PDF to Word, Word to PDF, PDF Compress, Image to Word/Excel — सब मुफ़्त और तेज़, बिना software install किए।{% endblock %}" />
<link rel="canonical" href="{% block canonical %}{{ site_url }}/{% endblock %}" />

<!-- Open Graph / Social sharing -->
<meta property="og:title" content="{% block og_title %}{{ self.title() }}{% endblock %}" />
<meta property="og:description" content="{% block og_description %}{{ self.meta_description() }}{% endblock %}" />
<meta property="og:type" content="website" />
<meta property="og:url" content="{{ self.canonical() }}" />

<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&family=Noto+Sans+Devanagari:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/static/css/style.css" />

{% block structured_data %}{% endblock %}
</head>
<body>

<header class="topbar">
  <div class="container topbar-inner">
    <a href="/" class="logo">📄 FileTools</a>
    <nav>
      <a href="/pdf-to-word">PDF to Word</a>
      <a href="/word-to-pdf">Word to PDF</a>
      <a href="/pdf-compress">PDF Compress</a>
      <a href="/image-to-word">Image to Word</a>
      <a href="/image-to-excel">Image to Excel</a>
    </nav>
  </div>
</header>

{% block content %}{% endblock %}

<footer class="footer">
  <div class="container">
    © 2026 FileTools — सभी अधिकार सुरक्षित &nbsp;·&nbsp;
    <a href="/pdf-to-word">PDF to Word</a> ·
    <a href="/word-to-pdf">Word to PDF</a> ·
    <a href="/pdf-compress">PDF Compress</a> ·
    <a href="/compress-pdf-to-100kb">Compress to 100KB</a> ·
    <a href="/compress-pdf-to-200kb">200KB</a> ·
    <a href="/image-to-word">Image to Word</a> ·
    <a href="/image-to-excel">Image to Excel</a>
  </div>
</footer>

<script src="/static/js/script.js"></script>
{% block extra_scripts %}{% endblock %}
</body>
</html>
