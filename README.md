{% extends "base.html" %}
{% import "_tool_card.html" as cards %}

{% block title %}FileTools — PDF to Word, Word to PDF, PDF Compress, Image to Word/Excel Online Free{% endblock %}
{% block meta_description %}मुफ़्त ऑनलाइन tools: PDF to Word, Word to PDF, PDF size compress (100KB/200KB/500KB तक), Image to Word, Image to Excel — बिना software install किए।{% endblock %}
{% block canonical %}{{ site_url }}/{% endblock %}

{% block structured_data %}
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "WebSite",
  "name": "FileTools",
  "url": "{{ site_url }}/"
}
</script>
{% endblock %}

{% block content %}
<section class="hero">
  <div class="container">
    <h1>अपनी Files सेकंडों में Convert करें</h1>
    <p>PDF ↔ Word, PDF Compress, Image से Word/Excel — सब कुछ मुफ़्त और तेज़, बिना किसी software install किए।</p>
  </div>
</section>

<section class="tools" id="tools">
  <div class="container tool-grid">
    {% for slug, tool in tools.items() %}
      {{ cards.tool_card(slug, tool) }}
    {% endfor %}
  </div>
</section>

<section class="how" id="how">
  <div class="container">
    <h2>कैसे काम करता है</h2>
    <div class="steps">
      <div class="step"><span>1</span>फ़ाइल चुनें</div>
      <div class="step"><span>2</span>Convert बटन दबाएं</div>
      <div class="step"><span>3</span>Result डाउनलोड करें</div>
    </div>
  </div>
</section>

<section class="popular-searches">
  <div class="container">
    <h2>ज़्यादा खोजे जाने वाले</h2>
    <div class="related-links">
      <a href="/compress-pdf-to-100kb">Compress PDF to 100KB</a>
      <a href="/compress-pdf-to-200kb">Compress PDF to 200KB</a>
      <a href="/compress-pdf-to-500kb">Compress PDF to 500KB</a>
      <a href="/compress-pdf-to-1mb">Compress PDF to 1MB</a>
    </div>
  </div>
</section>
{% endblock %}
