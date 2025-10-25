import os
from html import escape

def generate_standalone_index_html(test_results, output_dir="reports"):
    index_file = os.path.join(output_dir, "index.html")

    # --- Load individual test Markdown reports ---
    report_sections = []
    for i in range(len(test_results)):
        md_path = os.path.join(output_dir, f"test_case_{i+1}.md")
        if os.path.exists(md_path):
            with open(md_path, "r", encoding="utf-8") as f:
                content = f.read()
            # Escape Markdown for safe embedding
            escaped = escape(content)
            report_sections.append(f"""
<details>
  <summary>🧪 <b>Test Case {i+1}</b></summary>
  <article><script type="text/plain" class="md-src">{escaped}</script></article>
</details>
""")

    # --- Load the aggregated chart HTML ---
    agg_html_path = os.path.join(output_dir, "aggregated_metrics.html")
    agg_html_content = ""
    if os.path.exists(agg_html_path):
        with open(agg_html_path, "r", encoding="utf-8") as f:
            agg_html_content = f.read()

    # --- Write the complete HTML ---
    with open(index_file, "w", encoding="utf-8") as f:
        f.write(f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>🧭 GenAI Test Reports Dashboard</title>

<script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.8.0/styles/github.min.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.8.0/highlight.min.js"></script>

<style>
body {{
    font-family: "Segoe UI", Roboto, sans-serif;
    background-color: #fafafa;
    margin: 0; padding: 0;
}}
header {{
    background: linear-gradient(135deg, #0078D7, #00B7C3);
    color: white; text-align: center;
    padding: 1rem 0; font-size: 1.6rem;
    box-shadow: 0 2px 6px rgba(0,0,0,0.15);
}}
main {{
    display: flex; flex-direction: column;
    gap: 1rem; padding: 20px;
    max-width: 1000px; margin: auto;
}}
details {{
    background: white; border-radius: 8px;
    padding: 1rem; box-shadow: 0 2px 6px rgba(0,0,0,0.1);
}}
summary {{
    cursor: pointer; font-size: 1.2rem; font-weight: 600;
}}
pre {{
    background: #f4f4f4; padding: 10px;
    border-radius: 5px; overflow-x: auto;
}}
</style>
</head>
<body>

<header>📊 GenAI Test Report Dashboard</header>

<main>

<!-- Collapsible aggregated section -->
<details open>
  <summary>📈 <b>Aggregated Metric Distribution</b></summary>
  <div class="chart-container" style="margin-top:1rem;">
    {agg_html_content}
  </div>
</details>

<!-- Collapsible test reports -->
<details open>
  <summary>🔍 <b>Individual Test Reports</b></summary>
  <div style="margin-top:1rem;">
    {"".join(report_sections)}
  </div>
</details>

</main>

<script>
// Render Markdown from <script type="text/plain"> blocks
document.querySelectorAll('article').forEach(article => {{
  const src = article.querySelector('.md-src');
  if (!src) return;
  const raw = src.textContent;
  const rendered = marked.parse(raw);
  article.innerHTML = rendered;
  article.querySelectorAll('pre code').forEach(block => hljs.highlightElement(block));
}});
</script>

</body>
</html>""")

    print(f"✅ Generated fully working standalone dashboard: {index_file}")
