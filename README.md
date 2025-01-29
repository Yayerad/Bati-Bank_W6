<h1 align="center">Bati Bank Credit Scoring Model</h1>

<p align="center">
  <strong>AI-Powered Credit Risk Assessment System</strong>
</p>

<p align="center">
  <a href="#overview">Overview</a> •
  <a href="#folder-structure">Folder Structure</a> •
  <a href="#key-features">Key Features</a> •
  <a href="#installation">Installation</a> •
  <a href="#usage">Usage</a> •
  <a href="#api-documentation">API Documentation</a> •
  <a href="#contributing">Contributing</a> •
  <a href="#license">License</a>
</p>

---

<h2 id="overview">📝 Overview</h2>

<p>
  This project is a credit scoring system developed for <strong>Bati Bank</strong> to assess the creditworthiness of customers for their <em>buy-now-pay-later</em> service. The system uses machine learning models to predict the likelihood of customer default and assigns credit scores based on transaction data.
</p>

---

<h2 id="folder-structure">📂 Folder Structure</h2>

<pre>
.
├── <strong>notebooks/</strong>              # Jupyter notebooks
│   ├── eda.ipynb           # Exploratory Data Analysis
│   ├── feature_engineering.ipynb  # Feature engineering
│   └── model.ipynb         # Model development
├── <strong>scripts/</strong>               # Utility scripts
├── <strong>src/</strong>                   # Source code
│   └── <strong>data/</strong>             # Data files
│       ├── data.csv                # Raw data
│       └── engineered_transactions.csv  # Processed data
├── <strong>tests/</strong>                # Test cases
├── <strong>models/</strong>               # Trained models
│   ├── credit_scoring_lr.pkl      # Logistic Regression model
│   └── credit_scoring_rf.pkl      # Random Forest model
├── model_api.py           # FastAPI application
├── Dockerfile             # Docker configuration
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
</pre>

---

<h2 id="key-features">✨ Key Features</h2>

<ul>
  <li><strong>Notebook-based Workflow:</strong> Complete analysis in Jupyter notebooks</li>
  <li><strong>RFM Analysis:</strong> Recency, Frequency, Monetary feature engineering</li>
  <li><strong>Production-ready API:</strong> FastAPI endpoint for predictions</li>
  <li><strong>Dockerized Deployment:</strong> Containerized microservice architecture</li>
</ul>

---

<h2 id="installation">🚀 Installation</h2>

<h3>Prerequisites</h3>
<ul>
  <li>Python 3.9+</li>
  <li>Jupyter Lab (for notebook exploration)</li>
  <li>Docker (optional)</li>
</ul>

<h3>Setup</h3>

<ol>
  <li>Clone the repository:</li>
  <pre><code>git clone https://github.com/your-username/bati-bank-credit-scoring.git</code></pre>
  
  <li>Create virtual environment:</li>
  <pre><code>python -m venv .venv
source .venv/bin/activate  # Linux/MacOS
.\.venv\Scripts\activate   # Windows</code></pre>
  
  <li>Install dependencies:</li>
  <pre><code>pip install -r requirements.txt</code></pre>
</ol>

---

<h2 id="usage">💻 Usage</h2>

<h3>Notebook Execution</h3>
<p>Run notebooks in this order:</p>
<ol>
  <li><code>notebooks/eda.ipynb</code> - Data exploration</li>
  <li><code>notebooks/feature_engineering.ipynb</code> - Feature creation</li>
  <li><code>notebooks/model.ipynb</code> - Model training</li>
</ol>

<h3>API Deployment</h3>
<pre><code># Local deployment
uvicorn model_api:app --reload

# Docker deployment
docker build -t credit-api .
docker run -p 8000:8000 credit-api</code></pre>

---

<h2 id="api-documentation">📚 API Endpoints</h2>

<h3>Prediction Endpoints</h3>
<pre><code>POST /predict/lr     # Logistic Regression prediction
POST /predict/rf     # Random Forest prediction</code></pre>

<h3>Sample Request</h3>
<pre><code>curl -X POST "http://localhost:8000/predict/lr" \
-H "Content-Type: application/json" \
-d @src/data/sample_request.json</code></pre>

---

<h2 id="contributing">🤝 Contributing</h2>

<p>Follow these steps to contribute:</p>
<ol>
  <li>Create feature branch</li>
  <pre><code>git checkout -b feature/your-feature</code></pre>
  
  <li>Add tests for new features</li>
  <pre><code># Add tests to tests/ directory</code></pre>
  
  <li>Commit changes</li>
  <pre><code>git commit -m "Add amazing feature"</code></pre>
  
  <li>Push to branch</li>
  <pre><code>git push origin feature/your-feature</code></pre>
</ol>

---

<h2 id="license">📜 License</h2>

<p>
  Distributed under the MIT License. See <code>LICENSE</code> for more information.
</p>

<p align="center">
  Made with ❤️ by Your Name | Bati Bank Analytics Team
</p>
