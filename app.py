import streamlit as st
from utils.text_utils import extract_plain_text, clean_text
from utils.scoring import compute_match_score, find_missing_and_present
from utils.persistence import save_run

st.set_page_config(page_title="Resume ↔ JD Match Assistant", page_icon="🔎", layout="wide")

st.title("🔎 Resume ↔ Job Description Match Assistant")
st.caption("MVP scaffold — upload resume, paste JD, analyze, and save results.")

colA, colB = st.columns(2)

with colA:
    resume_file = st.file_uploader("Upload Resume (PDF/DOCX/TXT)", type=["pdf", "docx", "txt"])
    resume_text_raw = ""
    if resume_file is not None:
        # read once (file_uploader gives a stream)
        file_bytes = resume_file.read()
        resume_text_raw = extract_plain_text(resume_file.name, file_bytes)
    resume_text = clean_text(resume_text_raw) if resume_text_raw else ""

with colB:
    jd_text_raw = st.text_area("Paste Job Description", height=260, placeholder="Paste the full JD here…")
    jd_text = clean_text(jd_text_raw) if jd_text_raw else ""

st.markdown("---")

meta1, meta2, meta3 = st.columns([1, 1, 2])

with meta1:
    company = st.text_input("Company (optional)")

with meta2:
    role = st.text_input("Role (optional)")

with meta3:
    st.write("")
    run = st.button("⚡ Analyze Match", use_container_width=True)

if run:
    if not resume_text:
        st.error("Please upload a resume.")
    elif not jd_text:
        st.error("Please paste a job description.")
    else:
        score = compute_match_score(resume_text, jd_text)
        missing, present = find_missing_and_present(resume_text, jd_text)

        st.subheader(f"Overall Match: **{round(score * 100, 1)}%**")
        st.progress(min(max(score, 0.0), 1.0))

        c1, c2 = st.columns(2)
        with c1:
            st.markdown("### ✅ Present Keywords (naive)")
            st.write(", ".join(present) if present else "_None detected_")
        with c2:
            st.markdown("### ❗ Missing Keywords (naive)")
            st.write(", ".join(missing) if missing else "_None detected_")

        st.markdown("### ✍️ Suggestions (rule-of-thumb)")
        st.write("- Add a short **Summary** containing the most important missing terms.")
        st.write("- Mirror exact phrasing for critical skills (e.g., `Python`, `REST APIs`, `AWS`).")
        st.write("- Use quantifiable bullets where you add new terms.")

        save_run(company or "", role or "", score, missing)
        st.success("Saved to `data/job_applications.csv`.")

        with st.expander("📄 Preview extracted resume text"):
            st.write(resume_text_raw[:4000] if resume_text_raw else "_No text extracted_")
        with st.expander("🧾 Job description (original)"):
            st.write(jd_text_raw[:4000] if jd_text_raw else "_No JD provided_")
