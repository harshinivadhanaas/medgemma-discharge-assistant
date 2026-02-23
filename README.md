# 🏥 MedGemma Discharge Assistant

AI-powered discharge summary generator built for the 
MedGemma Impact Challenge 2026.

## What it does
Transforms raw clinical notes into structured discharge 
summaries in seconds using Google's MedGemma AI model.

## Live Demo
https://medgemma-discharge-assistant-cwljpsela9wp5knyojaw35.streamlit.app/

## Setup
1. Clone this repo
2. Install dependencies: `pip install -r requirements.txt`
3. Add your Gemini API key to `.streamlit/secrets.toml`:
```
   GEMINI_API_KEY = "your_key_here"
```
4. Run: `streamlit run app.py`

## Files
- `app.py` — Streamlit frontend
- `medgemma_client.py` — MedGemma API integration
- `requirements.txt` — Dependencies
- `test_api.py` — API connection test

## Built with
- Google MedGemma (via Gemini API)
- Streamlit
- Python
