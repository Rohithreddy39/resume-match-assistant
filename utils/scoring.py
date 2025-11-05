from typing import Tuple, List


# In the next step, we'll drop in TF-IDF + cosine similarity here.


def compute_match_score(resume_text: str, jd_text: str) -> float:
    """Temporary deterministic placeholder score (0..1)."""
    if not resume_text or not jd_text:
        return 0.0
    # naive token overlap as a deterministic stand-in
    r = set(resume_text.split())
    j = set(jd_text.split())
    if not r or not j:
        return 0.0
    inter = len(r & j)
    union = len(r | j)
    return inter / union


def find_missing_and_present(resume_text: str, jd_text: str, top_k: int = 30) -> Tuple[List[str], List[str]]:
    """Very naive keyword list until TF-IDF is wired in."""
    # take the most frequent JD words (simple heuristic)
    from collections import Counter
    jd_tokens = [t for t in jd_text.split() if len(t) > 2]
    freq = [w for w, _ in Counter(jd_tokens).most_common(top_k * 3)]


    rset = set(resume_text.split())
    present = [w for w in freq if w in rset][:top_k]
    missing = [w for w in freq if w not in rset][:top_k]
    return missing, present