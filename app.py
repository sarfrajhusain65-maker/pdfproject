{% macro tool_card(slug, tool, target_kb=None) %}
<div class="tool-card"
     data-endpoint="{{ tool.endpoint }}"
     data-accept="{{ tool.accept }}"
     data-outname="{{ tool.outname }}"
     {% if target_kb %}data-target-kb="{{ target_kb }}"{% endif %}>
  <div class="icon">{{ tool.icon }}</div>
  <h3>{{ tool.h1 or tool.title }}</h3>
  {% if not target_kb %}<p>{{ tool.meta_description }}</p>{% endif %}
  <label class="dropzone">
    <input type="file" accept="{{ tool.accept }}" hidden />
    <span class="dz-text">फ़ाइल चुनें या यहाँ drag करें</span>
  </label>

  {% if tool.has_quality or tool.has_target_kb %}
  <div class="compress-options">
    {% if tool.has_target_kb %}
    <label class="mini-label">Target size (KB) — खाली छोड़ें तो quality preset चलेगा</label>
    <input type="number" class="target-kb-input" placeholder="जैसे 100"
           {% if target_kb %}value="{{ target_kb }}"{% endif %} min="10" />
    {% endif %}
    {% if tool.has_quality %}
    <select class="quality-select">
      <option value="low">ज़्यादा compression (कम quality)</option>
      <option value="medium" selected>Balanced (recommended)</option>
      <option value="high">कम compression (बेहतर quality)</option>
    </select>
    {% endif %}
  </div>
  {% endif %}

  <div class="status"></div>
  <button class="convert-btn" disabled>{{ tool.button_text or "Convert करें" }}</button>
</div>
{% endmacro %}
