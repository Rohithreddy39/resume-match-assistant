# Resume ↔ Job Description Match Assistant

A Streamlit app that computes a match score between your resume and a job description, surfaces missing keywords, and saves results to a CSV job tracker.

## Features
- Upload resume (PDF/DOCX/TXT)
- Paste job description
- Get match score (TF-IDF + cosine similarity)
- See missing/present keywords and suggestions
- Auto-save runs to `data/job_applications.csv`

## Run locally
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt
streamlit run app.py
