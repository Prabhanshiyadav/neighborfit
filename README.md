# NeighborFit – Neighborhood Lifestyle Matcher

This full-stack app helps users find neighborhoods that match their lifestyle using a simple algorithm.

## Features

- User lifestyle input via sliders
- Matching algorithm
- Top 5 neighborhood suggestions
- Attractive Streamlit UI with sidebar and logo

## Tech Stack

- Python
- Streamlit
- CSV data

## Run Locally

```bash
streamlit run frontend/app.py
```

## Deploy

Use [Streamlit Cloud](https://share.streamlit.io/) to deploy `app.py`.

---

## 🧠 Learnings & Limitations

### ✅ What Worked Well
- Lightweight architecture using Python + Streamlit
- Simple scoring system is intuitive and interpretable
- Modular codebase with backend/frontend separation

### ⚠️ Limitations
- CSV data is static and basic
- No login system or user history
- Currently supports only 4 features for scoring

### 🚀 Future Improvements
- Real-time data APIs (e.g., neighborhood statistics)
- Scalable backend using FastAPI or Django
- Export results to PDF/Excel
- Map visualizations for matched neighborhoods
- Add multilingual UI for global users

