<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Court Data Fetcher - README</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 40px;
      line-height: 1.6;
    }
    h1, h2, h3 {
      color: #2c3e50;
    }
    code {
      background-color: #f4f4f4;
      padding: 2px 4px;
      border-radius: 4px;
      font-family: monospace;
    }
    pre {
      background-color: #f4f4f4;
      padding: 10px;
      border-radius: 5px;
      overflow-x: auto;
    }
    ul {
      margin-left: 20px;
    }
  </style>
</head>
<body>

  <h1>🧾 Court Data Fetcher</h1>
  <p>Fetch metadata and latest orders/judgments for cases from Indian High Court websites. Currently supports <strong>Delhi High Court</strong>.</p>

  <h2>🏁 Features</h2>
  <ul>
    <li>Scrape case details, filing date, status, orders, and more</li>
    <li>Handles CAPTCHA using a manual or automated strategy</li>
    <li>Mini-dashboard built with Django</li>
    <li>Reusable modular scraper logic</li>
  </ul>

  <h2>🔧 Setup Instructions</h2>
  <pre><code>git clone https://github.com/your-username/court-fetcher.git
cd court-fetcher
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt

# Set environment variables (see below)
python manage.py runserver
</code></pre>

  <h2>🤖 CAPTCHA Strategy</h2>
  <ul>
    <li>Currently uses <code>2Captcha</code> API (optional)</li>
    <li>Fallback: Manual entry if CAPTCHA fails or API not configured</li>
    <li>To automate, set the <code>2CAPTCHA_API_KEY</code> in environment</li>
  </ul>

  <h2>🌱 Sample .env</h2>
  <pre><code>2CAPTCHA_API_KEY=your_api_key_here
DJANGO_SECRET_KEY=your_django_secret_key
</code></pre>

  <h2>🏛️ Court Supported</h2>
  <ul>
    <li><strong>Delhi High Court</strong> ✅</li>
    <li>Other courts: coming soon...</li>
  </ul>

  <h2>📂 Sample URL Format</h2>
  <pre><code>/fetch/delhi/W.P.(C)/1234/2022/</code></pre>

  <h2>👨‍💻 Author</h2>
  <p>Developed by Ujjawal Dhami | Open to collaboration!</p>

</body>
</html>
