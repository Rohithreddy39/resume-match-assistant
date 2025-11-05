import os
import pandas as pd
from typing import List


CSV_PATH = "data/job_applications.csv"




def save_run(company: str, role: str, score: float, missing: List[str]) -> None:
	os.makedirs(os.path.dirname(CSV_PATH) or "data", exist_ok=True)
	# normalize missing to a list so .join and slicing are safe
	missing = missing or []
	row = {
		"timestamp": pd.Timestamp.now().isoformat(timespec="seconds"),
		"company": (company or "").strip(),
		"role": (role or "").strip(),
		"match_score": round(float(score), 4),
		"missing_keywords": ", ".join(missing[:20]),
	}
	if os.path.exists(CSV_PATH):
		df = pd.read_csv(CSV_PATH)
		df = pd.concat([df, pd.DataFrame([row])], ignore_index=True)
	else:
		df = pd.DataFrame([row])
	df.to_csv(CSV_PATH, index=False)