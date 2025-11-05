# Resume ↔ Job Description Match Assistant

A Streamlit app that computes a match score between your resume and a job description, surfaces missing keywords, and saves results to a CSV job tracker.

🧠 **What this project does**

A smart resume analyzer that compares your resume with a job description and shows:

✅ Match score

✅ Missing skills & keywords

✅ Present skills

✅ Action suggestions to improve resume targeting

✅ Saved job analysis history

🛠️ **Tech Stack**
- Python
- Streamlit
- Pandas
- Scikit-learn (for TF-IDF soon)
- PyPDF2 & python-docx (resume parsing)

🚀 **Features (MVP done)_**

1.Upload resume (PDF/DOCX/TXT)

2.Paste job description

3.Get keyword-based match score

4.See missing & present keywords

5.Save every run to CSV

🎯 **Upcoming Features (Roadmap)**

TF-IDF + Cosine Similarity scoring

Semantic scoring (Embeddings)

Resume improvement suggestions

Export analysis report (PDF/HTML)

Deploy on Streamlit Cloud

## Run locally
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt
streamlit run app.py

